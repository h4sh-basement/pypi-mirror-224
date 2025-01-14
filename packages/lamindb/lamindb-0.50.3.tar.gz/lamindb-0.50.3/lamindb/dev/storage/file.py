import os
import shutil
from pathlib import Path
from typing import Literal, Union

import anndata as ad
import fsspec
import pandas as pd
from lamin_utils import logger
from lamindb_setup import settings
from lamindb_setup.dev import StorageSettings
from lamindb_setup.dev.upath import UPath, infer_filesystem
from lnschema_core.models import File, Storage

try:
    from ._zarr import read_adata_zarr
except ImportError:

    def read_adata_zarr(filepath):  # type: ignore
        raise ImportError("Please install zarr: pip install zarr")


AUTO_KEY_PREFIX = ".lamindb/"


KNOWN_SUFFIXES = {
    # without readers
    ".txt",
    ".tsv",
    ".pdf",
    ".fastq",
    ".tar",
    ".zip",
    # with readers (see below)
    ".h5ad",
    ".parquet",
    ".csv",
    ".fcs",
    ".zarr",
    ".zrad",
}


def extract_suffix_from_path(path: Union[UPath, Path]) -> str:
    # this if-clause is based on https://stackoverflow.com/questions/31890341
    # the rest conscsiously deviates
    if len(path.suffixes) <= 2:
        return "".join(path.suffixes)
    else:
        msg = "file has more than two suffixes (path.suffixes), "
        # first check the 2nd-to-last suffix because it might be followed by .gz
        # or another compression-related suffix
        if path.suffixes[-2] in KNOWN_SUFFIXES:
            suffix = "".join(path.suffixes[-2:])
            msg += f"inferring:'{suffix}'"
        else:
            suffix = path.suffixes[-1]
            msg += f"using only last suffix: '{suffix}'"
        logger.warning(msg)
        return suffix


# add type annotations back asap when re-organizing the module
def auto_storage_key_from_file(file: File):
    if file.key is None:
        return f"{AUTO_KEY_PREFIX}{file.id}{file.suffix}"
    else:
        return file.key


def attempt_accessing_path(file: File, storage_key: str):
    if file.storage_id == settings.storage.id:
        path = settings.storage.key_to_filepath(storage_key)
    else:
        logger.warning("file.path is slightly slower for files outside default storage")
        storage = Storage.filter(id=file.storage_id).one()
        # find a better way than passing None to instance_settings in the future!
        storage_settings = StorageSettings(storage.root)
        path = storage_settings.key_to_filepath(storage_key)
    return path


def _str_to_path(path_str: str) -> Union[Path, UPath]:
    protocol = fsspec.utils.get_protocol(path_str)
    if protocol == "file":
        return Path(path_str)
    else:
        return UPath(path_str)


# add type annotations back asap when re-organizing the module
def filepath_from_file(file: File):
    if hasattr(file, "_local_filepath") and file._local_filepath is not None:
        return file._local_filepath.resolve()
    storage_key = auto_storage_key_from_file(file)
    path = attempt_accessing_path(file, storage_key)
    return path


def read_adata_h5ad(filepath, **kwargs) -> ad.AnnData:
    fs, filepath = infer_filesystem(filepath)

    with fs.open(filepath, mode="rb") as file:
        adata = ad.read_h5ad(file, backed=False, **kwargs)
        return adata


def print_hook(size: int, value: int, **kwargs):
    progress = value / size
    out = (
        f"... {kwargs['action']} {Path(kwargs['filepath']).name}:"
        f" {min(progress, 1.):4.2f}"
    )
    if progress >= 1:
        out += "\n"
    if "NBPRJ_TEST_NBPATH" not in os.environ:
        print(out, end="\r")


class ProgressCallback(fsspec.callbacks.Callback):
    def __init__(self, action: Literal["uploading", "downloading"]):
        super().__init__()
        self.action = action

    def branch(self, path_1, path_2, kwargs):
        kwargs["callback"] = fsspec.callbacks.Callback(
            hooks=dict(print_hook=print_hook), filepath=path_1, action=self.action
        )

    def call(self, *args, **kwargs):
        return None


def store_object(localpath: Union[str, Path], storagekey: str) -> float:
    """Store arbitrary file to configured storage location.

    Returns size in bytes.
    """
    storagepath = settings.instance.storage.key_to_filepath(storagekey)
    localpath = Path(localpath)

    if localpath.is_file():
        size = localpath.stat().st_size
    else:
        size = sum(f.stat().st_size for f in localpath.rglob("*") if f.is_file())

    if isinstance(storagepath, UPath):
        if localpath.suffix != ".zarr":
            cb = ProgressCallback("uploading")
        else:
            # todo: make proper progress bar for zarr
            cb = fsspec.callbacks.NoOpCallback()
        storagepath.upload_from(localpath, recursive=True, callback=cb)
    else:  # storage path is local
        storagepath.parent.mkdir(parents=True, exist_ok=True)
        if localpath.is_file():
            try:
                shutil.copyfile(localpath, storagepath)
            except shutil.SameFileError:
                pass
        else:
            if storagepath.exists():
                shutil.rmtree(storagepath)
            shutil.copytree(localpath, storagepath)
    return float(size)  # because this is how we store in the db


def delete_storage_using_key(file: File, storage_key: str):
    filepath = attempt_accessing_path(file, storage_key)
    delete_storage(filepath)


def delete_storage(storagepath: Union[Path, UPath]):
    """Delete arbitrary file."""
    if storagepath.is_file():
        storagepath.unlink()
    elif storagepath.is_dir():
        if isinstance(storagepath, UPath):
            storagepath.rmdir()
        else:
            shutil.rmtree(storagepath)
    else:
        raise FileNotFoundError(f"{storagepath} is not an existing path!")


def read_fcs(*args, **kwargs):
    try:
        import readfcs
    except ImportError:
        raise ImportError("Please install readfcs: pip install readfcs")
    return readfcs.read(*args, **kwargs)


def read_tsv(path: Union[str, Path]) -> pd.DataFrame:
    path_sanitized = Path(path)
    return pd.read_csv(path_sanitized, sep="\t")


def load_to_memory(filepath: Union[str, Path, UPath], stream: bool = False):
    """Load a file into memory.

    Returns the filepath if no in-memory form is found.
    """
    if isinstance(filepath, str):
        filepath = _str_to_path(filepath)

    if filepath.suffix in (".zarr", ".zrad"):
        stream = True
    elif filepath.suffix != ".h5ad":
        stream = False

    if not stream:
        # caching happens here if filename is a UPath
        # todo: make it safe when filepath is just Path
        cb = ProgressCallback("downloading")
        filepath = settings.instance.storage.cloud_to_local(filepath, callback=cb)

    READER_FUNCS = {
        ".csv": pd.read_csv,
        ".tsv": read_tsv,
        ".h5ad": read_adata_h5ad,
        ".parquet": pd.read_parquet,
        ".fcs": read_fcs,
        ".zarr": read_adata_zarr,
        ".zrad": read_adata_zarr,
    }

    reader = READER_FUNCS.get(filepath.suffix)
    if reader is None:
        return filepath
    else:
        return reader(filepath)
