import json
import logging
import os
import tarfile
from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from datetime import datetime, timezone
from itertools import groupby, islice
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import attrs
import sqlalchemy as sa
from sqlalchemy.schema import DropTable
from sqlalchemy.types import TypeEngine
from tqdm import tqdm

from dql.data_storage.schema import SignalsTable
from dql.node import DirType, get_path

if TYPE_CHECKING:
    from types import TracebackType

    from dql.listing import Listing

logger = logging.getLogger("dql")

PROCESSING_BATCH_SIZE = 1000  # Batch size for inserting entries.

INSERT_ITEMS = "insert"  # Indexing format adds new objects.
UPDATE_ITEMS = "update"  # Indexing format extends objects with new properties.


def flatten_signals(d, parent_key="", delimiter="."):
    """
    Special flatten dict function adopted for flattening signals where we skip
    some fields if conditions are met (empty fields, list of subobjects etc.)
    """
    items = []
    for key, value in d.items():
        new_key = parent_key + delimiter + key if parent_key else key
        if value is None:
            continue
        if (isinstance(value, dict) or isinstance(value, list)) and not value:
            # skipping empty lists and dicts
            continue
        elif isinstance(value, list) and isinstance(value[0], list):
            # skipping list of lists
            continue
        elif isinstance(value, list) and isinstance(value[0], dict):
            # skipping list of dicts
            continue
        elif isinstance(value, dict):
            items.extend(flatten_signals(value, new_key, delimiter=delimiter).items())
        else:
            items.append((new_key, value))

    return dict(items)


def get_columns(signals: Dict[str, Any]) -> List[Tuple[str, TypeEngine]]:
    """
    Get list of sqlalchemy table column name - type pairs from signals/annotation dict
    It accepts flattened dict so it should not have any subobjects or list of
    objects
    """

    def get_sa_type(value: Any) -> TypeEngine:
        type_map = {
            float: sa.Float(),
            int: sa.Integer(),
            str: sa.String(),
            list: sa.JSON(),
            bool: sa.Boolean(),
        }

        t = type(value)
        if t not in type_map:
            raise Exception(
                f"Couldn't map type {t} of value {value} to sqlalchemy column type"
            )

        return type_map[t]

    return [
        (col_name, get_sa_type(col_value)) for col_name, col_value in signals.items()
    ]


def get_union_columns(
    signals_list: Iterable[Dict[str, Any]]
) -> List[Tuple[str, TypeEngine]]:
    """
    Function that receives list of signal/annotation dicts with arbitrary flattened
    schemas and returns list of all flattened sqlalchemy columns to be created for them
    Each column is represented with a tuple of name and type
    """
    result = []
    seen = set()
    for s in signals_list:
        for name, sa_type in get_columns(s):
            key = (name, type(sa_type))
            if key not in seen:
                result.append((name, sa_type))
                seen.add(key)
    return result


class Operation(AbstractContextManager, ABC):
    """Operation to apply to data generated by processors."""

    # This is defined outside the IndexingFormat class to allow
    # for batching operations.
    @abstractmethod
    async def __call__(self, items: Iterable[Any]):
        pass


class InsertNodes(Operation):
    """Operation that inserts nodes."""

    def __init__(self, listing: "Listing"):
        self.listing = listing

    async def __call__(self, items):
        await self.listing.data_storage.insert_entries(items)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional["TracebackType"],
    ):
        self.listing.data_storage.inserts_done()


class InsertSignals(Operation):
    """Insert rows into a signals table."""

    def __init__(self, listing: "Listing", columns=()):
        self.listing = listing
        self.columns = columns
        self.table: SignalsTable

    async def __call__(self, items):
        self.insert(items, self.columns)

    def insert(self, items, columns):
        for col in columns:
            # id column should be created automatically so skipping it
            if col[0] != "id":
                # this also refreshes metadata (same instance as in self.table)
                # so we will have the newest version of self.table.table
                self.listing.data_storage.add_column(
                    self.table.table,
                    col[0],
                    col[1],
                )

        # adding a default values for missing columns
        for item in items:
            for c in columns:
                if c[0] not in item:
                    item[c[0]] = None

        q = self.table.insert().values(items)
        self.listing.data_storage.execute(q)

    def __enter__(self) -> "Operation":
        self.table = self.listing.data_storage.create_signals_table()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional["TracebackType"],
    ):
        ds = self.listing.data_storage
        try:
            if exc_val is None:
                ds.extend_index_with_signals(ds.nodes, self.table)
        finally:
            ds.execute(DropTable(self.table.table))


class InsertJSONSignals(InsertSignals):
    """Insert rows into a signals table with extracted JSON signals."""

    signal_prefix = "a_"
    subobject_delimiter = "__"

    async def __call__(self, items):
        items = self.process_items(items)
        self.columns = (*self.columns, *get_union_columns(items))
        self.insert(items, self.columns)

    def _prefix_col_name(self, col_name):
        if col_name == "id":
            return col_name
        return self.signal_prefix + col_name

    def process_items(self, items):
        items = [
            flatten_signals(item, delimiter=self.subobject_delimiter) for item in items
        ]
        return [
            {self._prefix_col_name(key): val for (key, val) in item.items()}
            for item in items
        ]


T = TypeVar("T")


class IndexingFormat(ABC, Generic[T]):
    """
    Indexing formats allow additional transformations on indexed
    objects, such as listing contents of archives.
    """

    @abstractmethod
    def begin(self, listing: "Listing") -> Operation:
        """
        Preprare for processing the nodes.
        This function returns an object that acts as a callable
        on batches of produced items and doubles as a context manager
        to cleanup after processing.
        """

    @abstractmethod
    def filter(self, listing: "Listing", paths: List[str]) -> Iterator[T]:
        """Create a list of entries to process"""

    @abstractmethod
    def process(self, listing, entries):
        """Process an entry and return additional entries to store."""


@attrs.define
class ArchiveInfo:
    parent: str
    name: str
    id: int
    is_latest: bool
    checksum: str
    partial_id: int

    @property
    def path(self):
        return get_path(self.parent, self.name)


ARCHIVE_INFO_FIELDS = [attr.name for attr in attrs.fields(ArchiveInfo)]


class TarFiles(IndexingFormat[ArchiveInfo]):
    """
    TarFiles indexes buckets containing uncompressed tar archives. The contents of
    the archives is indexed as well.
    """

    processing_message = "Indexing tarball files"

    def begin(self, listing: "Listing") -> Operation:
        return InsertNodes(listing)

    def filter(self, listing: "Listing", paths: List[str]) -> Iterator[ArchiveInfo]:
        for path in paths:
            for node in listing.expand_path(path):
                found = listing.find(
                    node,
                    ARCHIVE_INFO_FIELDS,
                    names=["*.tar"],
                )
                for row in found:
                    yield ArchiveInfo(*row)

    def process(self, listing: "Listing", entries):
        for entry in entries:
            yield from self.process_entry(listing, entry)

    def process_entry(
        self, listing: "Listing", parent: ArchiveInfo
    ) -> Iterator[Dict[str, Any]]:
        client = listing.client
        # Download tarball to local cache first.
        tar_hash = client.download(
            parent.path, vtype="", location=None, checksum=parent.checksum
        )
        parent.checksum = tar_hash
        listing.data_storage.update_node(
            parent.id, {"dir_type": DirType.TAR_ARCHIVE, "checksum": tar_hash}
        )
        with client.open_object(
            parent.path, vtype="", location=None, checksum=tar_hash
        ) as f:
            with tarfile.open(fileobj=f, mode="r:") as tar:
                for info in tar:
                    if info.isdir():
                        yield self.tardir_from_info(info, parent)
                    elif info.isfile():
                        yield self.tarmember_from_info(info, parent)

    def tarmember_from_info(self, info, parent: ArchiveInfo) -> Dict[str, Any]:
        location = json.dumps(
            [
                {
                    "offset": info.offset_data,
                    "size": info.size,
                    "type": "tar",
                    "parent": parent.path,
                    "parent_hash": parent.checksum,
                },
            ]
        )
        full_path = f"{parent.path}/{info.name}"
        parent_dir, name = full_path.rsplit("/", 1)
        return {
            "vtype": "tar",
            "dir_type": DirType.FILE,
            "parent_id": parent.id,
            "parent": parent_dir,
            "name": name,
            "checksum": "",
            "etag": "",
            "version": "",
            "is_latest": parent.is_latest,
            "last_modified": datetime.fromtimestamp(info.mtime, timezone.utc),
            "size": info.size,
            "owner_name": info.uname,
            "owner_id": str(info.uid),
            "location": location,
            "partial_id": parent.partial_id,
        }

    def tardir_from_info(self, info, parent: ArchiveInfo) -> Dict[str, Any]:
        full_path = f"{parent.path}/{info.name}".rstrip("/")
        parent_dir, name = full_path.rsplit("/", 1)
        return {
            "vtype": "tar",
            "dir_type": DirType.DIR,
            "parent_id": parent.id,
            "parent": parent_dir,
            "name": name,
            "checksum": "",
            "etag": "",
            "version": "",
            "is_latest": parent.is_latest,
            "last_modified": datetime.fromtimestamp(info.mtime, timezone.utc),
            "size": info.size,
            "owner_name": info.uname,
            "owner_id": str(info.uid),
            "partial_id": parent.partial_id,
        }


@attrs.define
class ObjectInfo:
    parent: str
    name: str
    id: int
    vtype: str
    location: str

    @property
    def path(self):
        return get_path(self.parent, self.name)


OBJECT_INFO_FIELDS = [attr.name for attr in attrs.fields(ObjectInfo)]


class JSONPair(IndexingFormat[ObjectInfo]):
    """
    Load signals from .json files and attach them to objects with the same base name.
    """

    processing_message = "Loading json annotations"

    IGNORED_EXTS = [".json", ".txt"]  # File extensions not to attach loaded signals to.

    def begin(self, listing: "Listing") -> Operation:
        return InsertJSONSignals(listing)

    def filter(self, listing: "Listing", paths: List[str]) -> Iterator[ObjectInfo]:
        for path in paths:
            for node in listing.expand_path(path):
                found = listing.find(
                    node,
                    OBJECT_INFO_FIELDS,
                    order_by=["parent", "name"],
                )
                for row in found:
                    yield ObjectInfo(*row)

    def process(self, listing: "Listing", entries):
        for _, group in groupby(entries, self._group):
            yield from self._process_group(listing, group)

    def _process_group(self, listing: "Listing", group: Iterable[ObjectInfo]) -> Any:
        # Create a map of extension to object info.
        nodes = {os.path.splitext(obj.name)[1]: obj for obj in group}
        json_obj = nodes.get(".json")
        if not json_obj:
            # No .json file in group. Ignore.
            return
        with listing.client.open_object(
            json_obj.path, json_obj.vtype, json_obj.location
        ) as f:
            data = json.load(f)
            if not isinstance(data, dict):
                # .json file contains something other than a json object. Ignore.
                return

        for ext, node in nodes.items():
            if ext in self.IGNORED_EXTS:
                continue
            d = data.copy()
            d["id"] = node.id
            yield d

    def _group(self, entry):
        """
        Group entries by paths sans the extension.
        This way 'path/000.jpg' and 'path/000.json' will be grouped
        together.
        """
        return os.path.splitext(entry.path)[0]


async def apply_processors(
    listing: "Listing", path: str, processors: List[IndexingFormat]
):
    for processor in processors:
        msg = getattr(processor, "processing_message", None or "Processing")
        with processor.begin(listing) as op:
            with tqdm(desc=msg, unit=" objects") as pbar:
                entries = processor.filter(listing.clone(), [path])
                results = processor.process(listing.clone(), entries)
                for batch in _batch(results, PROCESSING_BATCH_SIZE):
                    pbar.update(len(batch))
                    await op(batch)


def _batch(it, size):
    while batch := list(islice(it, size)):
        yield batch


indexer_formats: Dict[str, Union[List[IndexingFormat], IndexingFormat]] = {
    "tar-files": TarFiles(),
    "json-pair": JSONPair(),
    "webdataset": [TarFiles(), JSONPair()],
}
