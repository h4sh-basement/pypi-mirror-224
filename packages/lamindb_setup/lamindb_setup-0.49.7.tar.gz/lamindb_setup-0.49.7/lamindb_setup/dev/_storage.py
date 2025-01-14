import os
from pathlib import Path
from typing import Any, Literal, Optional, Union

from appdirs import AppDirs
from botocore.exceptions import NoCredentialsError
from lamin_utils import logger

from .upath import UPath

DIRS = AppDirs("lamindb", "laminlabs")


class StorageSettings:
    """Manage cloud or local storage settings."""

    def __init__(
        self,
        root: Union[str, Path, UPath],
        region: Optional[str] = None,
    ):
        if isinstance(root, UPath):
            root_path = root
        elif isinstance(root, Path):
            root.mkdir(parents=True, exist_ok=True)  # resolve fails for nonexisting dir
            root_path = root.resolve()
        elif isinstance(root, str):
            root_path = Storage._str_to_path(root)
        else:
            raise ValueError("root should be of type Union[str, Path, UPath].")
        self._root = root_path
        self._region = region
        # would prefer to type below as Registry, but need to think through import order
        self._record: Optional[Any] = None

    @staticmethod
    def _str_to_path(storage: str) -> Union[Path, UPath]:
        if storage.startswith("s3://"):
            # for new buckets there could be problems if the region is not specified
            storage_root = UPath(storage, cache_regions=True)
            try:
                storage_root.stat()
            except NoCredentialsError:
                logger.warning("did not find aws credentials, using anonymous")
                storage_root = UPath(storage_root, anon=True)
        elif storage.startswith("gs://"):
            storage_root = UPath(storage)
        else:  # local path
            os.makedirs(storage, exist_ok=True)  # resolve fails for nonexisting dir
            storage_root = Path(storage).resolve()
        return storage_root

    @property
    def id(self) -> str:
        """Storage id."""
        return self.record.id

    @property
    def record(self) -> Any:
        """Storage record."""
        if self._record is None:
            # dynamic import because of import order
            from lnschema_core.models import Storage

            self._record = Storage.objects.get(root=self.root_as_str)
        return self._record

    @property
    def root(self) -> Union[Path, UPath]:
        """Root storage location."""
        return self._root

    def _set_fs_kwargs(self, **kwargs):
        """Set additional fsspec arguments for cloud root.

        Example:

        >>> ln.setup.settings.storage._set_fs_kwargs(  # any fsspec args
        >>>    profile="some_profile", cache_regions=True
        >>> )
        """
        if isinstance(self._root, UPath):
            self._root = UPath(self._root, **kwargs)

    @property
    def root_as_str(self) -> str:
        """Formatted root string."""
        return self.root.as_posix().rstrip("/")

    @property
    def cache_dir(
        self,
    ) -> Path:
        """Cache root, a local directory to cache cloud files."""
        cache_dir = Path(DIRS.user_cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    @property
    def is_cloud(self) -> bool:
        """`True` if `storage_root` is in cloud, `False` otherwise."""
        return isinstance(self.root, UPath)

    @property
    def region(self) -> Optional[str]:
        """Storage region."""
        return self._region

    @property
    def type(self) -> Literal["s3", "gs", "local"]:
        """AWS S3 vs. Google Cloud vs. local.

        Returns "s3" or "gs" or "local".
        """
        root_str = str(self.root)
        if root_str.startswith("s3://"):
            return "s3"
        elif root_str.startswith("gs://"):
            return "gs"
        else:
            return "local"

    def key_to_filepath(self, filekey: Union[Path, UPath, str]) -> Union[Path, UPath]:
        """Cloud or local filepath from filekey."""
        return self.root / filekey

    def cloud_to_local(self, filepath: Union[Path, UPath], **kwargs) -> Path:
        """Local (cache) filepath from filepath."""
        local_filepath = self.cloud_to_local_no_update(filepath)  # type: ignore
        if isinstance(filepath, UPath):
            local_filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.synchronize(local_filepath, **kwargs)
        return local_filepath

    # conversion to Path via cloud_to_local() would trigger download
    # of remote file to cache if there already is one
    # in pure write operations that update the cloud, we don't want this
    # hence, we manually construct the local file path
    # using the `.parts` attribute in the following line
    def cloud_to_local_no_update(self, filepath: Union[Path, UPath]) -> Path:
        if isinstance(filepath, UPath):
            return self.cache_dir.joinpath(filepath._url.netloc, *filepath.parts[1:])  # type: ignore # noqa
        return filepath

    def local_filepath(self, filekey: Union[Path, UPath, str]) -> Path:
        """Local (cache) filepath from filekey: `local(filepath(...))`."""
        return self.cloud_to_local(self.key_to_filepath(filekey))


# below is for backward compat
Storage = StorageSettings
