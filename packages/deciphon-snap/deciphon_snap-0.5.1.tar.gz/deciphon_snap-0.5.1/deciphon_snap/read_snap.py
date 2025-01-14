from fsspec.implementations.cached import WholeFileCacheFileSystem
from fsspec.implementations.zip import ZipFileSystem

from deciphon_snap.path_like import PathLike
from deciphon_snap.snap_file import SnapFile

__all__ = ["read_snap"]


def read_snap(filename: PathLike):
    return SnapFile(WholeFileCacheFileSystem(fs=ZipFileSystem(filename)))
