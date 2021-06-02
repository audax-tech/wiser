from __future__ import annotations

from pathlib import Path
from builtins import property


class StorageLocation:
    def __init__(
        self, prefix: str, bucket: str, blob_name: str, folders: str, filename: str
    ):
        self._prefix = prefix
        self._bucket = bucket
        self._blob_name = str(Path(blob_name))
        self._folders = str(Path(folders))
        self._filename = filename

    @property
    def prefix(self):
        return self._prefix

    @property
    def bucket(self):
        return self._bucket

    @property
    def folders(self):
        return self._folders

    @property
    def filename(self):
        return self._filename

    @property
    def blob_name(self):
        return self._blob_name

    @property
    def complete_path(self):
        return str(Path(self._prefix).joinpath(self._bucket).joinpath(self._blob_name))


class StorageLocationBuilder:
    def __init__(self):
        self._prefix = "gs://"
        self._bucket = None
        self._blob_name = None

    def set_prefix(self, prefix: str) -> StorageLocationBuilder:
        self._prefix = prefix
        return self

    def set_bucket(self, bucket: str) -> StorageLocationBuilder:
        self._bucket = bucket
        return self

    def set_blob_name(self, blob_name: str) -> StorageLocationBuilder:
        self._blob_name = blob_name
        return self

    def build(self) -> StorageLocation:
        # Validating setting
        if self._bucket is None:
            raise ValueError("Bucket not set")

        if self._blob_name is None:
            raise ValueError("Blob name not set")

        # Getting filename from blob_name
        folders, filename = self._blob_name.split("/")

        return StorageLocation(
            prefix=self._prefix,
            bucket=self._bucket,
            folders=folders,
            blob_name=self._blob_name,
            filename=filename,
        )
