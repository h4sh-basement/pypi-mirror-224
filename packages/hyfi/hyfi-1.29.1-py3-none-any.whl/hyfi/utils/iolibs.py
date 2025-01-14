"""File I/O functions"""
import errno
import json
import os
import re
import shutil
import stat
import sys
import time
from glob import glob
from pathlib import Path, PosixPath, WindowsPath
from types import TracebackType
from typing import Callable, Iterator, List, Optional, Tuple, Union

from hyfi.utils.logging import LOGGING
from hyfi.utils.types import PathLikeType

logger = LOGGING.getLogger(__name__)


class IOLIBs:
    @staticmethod
    def is_valid_regex(expr: str) -> bool:
        """Check if a string is a valid regular expression"""
        try:
            if expr.startswith("r:"):
                expr = expr[2:]
            else:
                return False
            re.compile(expr)
            return True
        except re.error:
            return False

    @staticmethod
    def glob_re(
        pattern: str,
        base_dir: str,
        recursive: bool = False,
    ) -> list:
        """Glob files matching a regular expression"""
        if IOLIBs.is_valid_regex(pattern):
            pattern = pattern[2:]
            rpattern = re.compile(pattern)  # type: ignore
            files = []
            if recursive:
                for dirpath, _, filenames in os.walk(base_dir):
                    files += [
                        os.path.join(dirpath, file)
                        for file in filenames
                        if rpattern.search(file)
                    ]
            else:
                files = [
                    os.path.join(base_dir, file)
                    for file in os.listdir(base_dir)
                    if rpattern.search(file)
                ]
        else:
            file = os.path.join(base_dir, pattern)
            files = glob(file, recursive=recursive)
        return files

    @staticmethod
    def get_filepaths(
        filename_patterns: Union[List[PathLikeType], PathLikeType],
        base_dir: Optional[Union[str, PosixPath, WindowsPath]] = None,
        recursive: bool = True,
        use_cached: bool = False,
        verbose: bool = False,
        **kwargs,
    ) -> List[str]:
        """Get a list of filepaths from a list of filename patterns"""
        if filename_patterns is None:
            raise ValueError("filename_patterns must be specified")
        if isinstance(filename_patterns, (PosixPath, WindowsPath)):
            filename_patterns = str(filename_patterns)
        if isinstance(filename_patterns, str):
            filename_patterns = [filename_patterns]
        filepaths = []
        base_dir = str(base_dir) if base_dir else ""
        for f_pattern in filename_patterns:
            f_pattern = str(f_pattern)
            if f_pattern.startswith("http") and not use_cached:
                filepaths.append(f_pattern)
            else:
                if f_pattern.startswith("http"):
                    filepath = IOLIBs.cached_path(f_pattern, **kwargs)
                else:
                    filepath = os.path.join(base_dir, f_pattern)
                if isinstance(filepath, str) and os.path.exists(filepath):
                    if Path(filepath).is_file():
                        filepaths.append(filepath)
                else:
                    if os.path.dirname(f_pattern) != "":
                        _dir = os.path.dirname(f_pattern)
                        f_pattern = os.path.basename(f_pattern)
                        base_dir = os.path.join(base_dir, _dir)
                    filepaths += IOLIBs.glob_re(
                        f_pattern, base_dir, recursive=recursive
                    )
        filepaths = [
            fp for fp in filepaths if Path(fp).is_file() or fp.startswith("http")
        ]
        if verbose:
            logger.info(f"Processing [{len(filepaths)}] files from {filename_patterns}")

        return filepaths

    @staticmethod
    def get_files_from_archive(archive_path: str, filetype: str = ""):
        """Get a list of files from an archive"""
        import tarfile
        from zipfile import ZipFile

        if ".tar.gz" in archive_path:
            logger.info(f"::Extracting files from {archive_path} with tar.gz")
            archive_handle = tarfile.open(archive_path, "r:gz")
            files = [
                (file, file.name)
                for file in archive_handle.getmembers()
                if file.isfile()
            ]
            open_func = archive_handle.extractfile
        elif ".tar.bz2" in archive_path:
            logger.info(f"::Extracting files from {archive_path} with tar.bz2")
            archive_handle = tarfile.open(archive_path, "r:bz2")
            files = [
                (file, file.name)
                for file in archive_handle.getmembers()
                if file.isfile()
            ]
            open_func = archive_handle.extractfile
        elif ".zip" in archive_path:
            logger.info(f"::Extracting files from {archive_path} with zip")
            archive_handle = ZipFile(archive_path)
            files = [
                (file, file.encode("cp437").decode("euc-kr"))
                for file in archive_handle.namelist()
            ]
            open_func = archive_handle.open
        else:
            # print(f'::{archive_path} is not archive, use generic method')
            files = [(archive_path, os.path.basename(archive_path))]
            archive_handle = None
            open_func = None
        if filetype:
            files = [file for file in files if filetype in file[1]]

        return files, archive_handle, open_func

    @staticmethod
    def read(uri, mode="rb", encoding=None, head=None, **kwargs) -> bytes:
        """Read data from a file or url"""
        uri = str(uri)
        if uri.startswith("http"):
            import requests

            if mode == "r" and head is not None and isinstance(head, int):
                r = requests.get(uri, stream=True)
                r.raw.decode_content = True
                return r.raw.read(head)
            return requests.get(uri, **kwargs).content
        # elif uri.startswith("s3://"):
        #     import boto3

        #     s3 = boto3.resource("s3")
        #     bucket, key = uri.replace("s3://", "").split("/", 1)
        #     obj = s3.Object(bucket, key)
        #     return obj.get()["Body"].read()
        else:
            with open(uri, mode=mode, encoding=encoding) as f:
                if mode == "r" and head is not None and isinstance(head, int):
                    return f.read(head)
                return f.read()

    @staticmethod
    def walk_to_root(path: str) -> Iterator[str]:
        """
        Yield directories starting from the given directory up to the root
        """
        if not os.path.exists(path):
            raise IOError("Starting path not found")

        if os.path.isfile(path):
            path = os.path.dirname(path)

        last_dir = None
        current_dir = os.path.abspath(path)
        while last_dir != current_dir:
            yield current_dir
            parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
            last_dir, current_dir = current_dir, parent_dir

    @staticmethod
    def is_file(a, *p) -> bool:
        """Check if path is a file"""
        _path = os.path.join(a, *p)
        return Path(_path).is_file()

    @staticmethod
    def is_dir(a, *p) -> bool:
        """Check if path is a directory"""
        _path = os.path.join(a, *p)
        return Path(_path).is_dir()

    @staticmethod
    def check_path(_path: str, alt_path: str = "") -> str:
        """Check if path exists, return alt_path if not"""
        return _path if os.path.exists(_path) else alt_path

    @staticmethod
    def mkdir(_path: str) -> str:
        """Create directory if it does not exist"""
        if _path is None:
            return ""
        Path(_path).mkdir(parents=True, exist_ok=True)
        return _path

    @staticmethod
    def exists(a, *p) -> bool:
        """Check if path exists"""
        if a is None:
            return False
        _path = os.path.join(a, *p)
        return os.path.exists(_path)

    @staticmethod
    def join_path(a, *p) -> str:
        """Join path components intelligently."""
        if not p or p[0] is None:
            return a
        p = [str(_p) for _p in p]
        return os.path.join(*p) if a is None else os.path.join(a, *p)

    @staticmethod
    def copy(
        src: PathLikeType,
        dst: PathLikeType,
        follow_symlinks: bool = True,
    ):
        """
        Copy a file or directory. This is a wrapper around shutil.copy.
        If you need to copy an entire directory (including all of its contents), or if you need to overwrite existing files in the destination directory, shutil.copy() would be a better choice.

        Args:
                src: Path to the file or directory to be copied.
                dst: Path to the destination directory. If the destination directory does not exist it will be created.
                follow_symlinks: Whether or not symlinks should be followed
        """
        src = str(src)
        dst = str(dst)
        IOLIBs.mkdir(dst)
        shutil.copy(src, dst, follow_symlinks=follow_symlinks)
        logger.info(f"copied {src} to {dst}")

    @staticmethod
    def copyfile(
        src: PathLikeType,
        dst: PathLikeType,
        follow_symlinks: bool = True,
    ):
        """
        Copy a file or directory. This is a wrapper around shutil.copyfile.
        If you want to copy a single file from one location to another, shutil.copyfile() is the appropriate function to use.

        Args:
                src: Path to the file or directory to copy.
                dst: Path to the destination file or directory. If the destination file already exists it will be overwritten.
                follow_symlinks: Whether to follow symbolic links or not
        """
        src = str(src)
        dst = str(dst)
        shutil.copyfile(src, dst, follow_symlinks=follow_symlinks)
        logger.info(f"copied {src} to {dst}")

    @staticmethod
    def copy_file(
        src: PathLikeType,
        dst: PathLikeType,
        follow_symlinks: bool = True,
    ) -> None:
        """Copy one file to another place."""
        src = str(src)
        dst = str(dst)
        shutil.copy2(src, dst, follow_symlinks=follow_symlinks)

    @staticmethod
    def get_modified_time(path):
        """Return the modification time of a file"""
        if not os.path.exists(path):
            return None
        modTimesinceEpoc = os.path.getmtime(path)
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(modTimesinceEpoc))

    @staticmethod
    def handle_remove_readonly(
        func: Callable, path: str, exc: Tuple[BaseException, OSError, TracebackType]
    ) -> None:
        """Handle errors when trying to remove read-only files through `shutil.rmtree`.

        This handler makes sure the given file is writable, then re-execute the given removal function.

        Arguments:
            func: An OS-dependant function used to remove a file.
            path: The path to the file to remove.
            exc: A `sys.exc_info()` object.
        """
        excvalue = exc[1]
        if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
            func(path)
        else:
            raise

    @staticmethod
    def readlink(link: Path) -> Path:
        """A custom version of os.readlink/pathlib.Path.readlink.

        pathlib.Path.readlink is what we ideally would want to use, but it is only available on python>=3.9.
        os.readlink doesn't support Path and bytes on Windows for python<3.8
        """
        if sys.version_info >= (3, 9):
            return link.readlink()
        elif sys.version_info >= (3, 8) or os.name != "nt":
            return Path(os.readlink(link))
        else:
            return Path(os.readlink(str(link)))

    @staticmethod
    def extractall(
        path: str,
        dest: str = "",
        force_extract: bool = False,
    ):
        """Extract archive file.

        Parameters
        ----------
        path: str
            Path of archive file to be extracted.
        dest: str, optional
            Directory to which the archive file will be extracted.
            If None, it will be set to the parent directory of the archive file.
        """
        import tarfile
        from zipfile import ZipFile

        if dest is None:
            dest = os.path.dirname(path)

        if path.endswith(".zip"):
            opener, mode = ZipFile, "r"
        elif path.endswith(".tar"):
            opener, mode = tarfile.open, "r"
        elif path.endswith(".tar.gz") or path.endswith(".tgz"):
            opener, mode = tarfile.open, "r:gz"
        elif path.endswith(".tar.bz2") or path.endswith(".tbz"):
            opener, mode = tarfile.open, "r:bz2"
        else:
            logger.warning(
                f"Could not extract '{path}' as no appropriate extractor is found"
            )
            return path, None

        def namelist(f):
            return (
                f.namelist() if isinstance(f, ZipFile) else [m.path for m in f.members]
            )

        def filelist(f):
            files = []
            for fname in namelist(f):
                fname = os.path.join(dest, fname)
                files.append(fname)
            return files

        extraction_name = Path(path).stem
        extraction_path = f"{dest}/{extraction_name}"
        if extraction_path and (
            os.path.isdir(extraction_path)
            and os.listdir(extraction_path)
            and not force_extract
        ):
            files = [
                os.path.join(dirpath, filename)
                for dirpath, _, filenames in os.walk(extraction_path)
                for filename in filenames
            ]

            return dest, files

        with opener(path, mode) as f:  # type: ignore
            f.extractall(path=dest)

        return dest, filelist(f)

    @staticmethod
    def save_wordlist(
        words: List[str],
        filepath: Union[str, PosixPath, WindowsPath, Path],
        sort: bool = True,
        encoding: str = "utf-8",
        verbose: bool = True,
    ):
        """Save the word list to the file."""
        if sort:
            words = sorted(words)
        if verbose:
            logger.info(
                "Save the list to the file: %s, no. of words: %s", filepath, len(words)
            )
        with open(filepath, "w", encoding=encoding) as fo_:
            for word in words:
                fo_.write(word + "\n")

    @staticmethod
    def load_wordlist(
        filepath: Union[str, PosixPath, WindowsPath, Path],
        sort: bool = True,
        lowercase: bool = False,
        unique: bool = True,
        remove_tag: bool = False,
        max_ngram_to_include: Optional[int] = None,
        ngram_delimiter: str = ";",
        remove_delimiter: bool = False,
        encoding: str = "utf-8",
        verbose: bool = True,
    ) -> List[str]:
        """Load the word list from the file."""
        filepath = Path(filepath)
        if not filepath.is_file():
            logger.warning("File not found: %s", filepath)
            return []

        with open(filepath, encoding=encoding) as fo_:
            words = [word.strip().split()[0] for word in fo_ if len(word.strip()) > 0]

        if verbose:
            logger.info("Loaded the file: %s, No. of words: %s", filepath, len(words))

        return IOLIBs.process_wordlist(
            words,
            sort=sort,
            lowercase=lowercase,
            unique=unique,
            remove_tag=remove_tag,
            max_ngram_to_include=max_ngram_to_include,
            ngram_delimiter=ngram_delimiter,
            remove_delimiter=remove_delimiter,
            verbose=verbose,
        )

    @staticmethod
    def process_wordlist(
        words: List[str],
        sort: bool = True,
        lowercase: bool = False,
        unique: bool = True,
        remove_tag: bool = False,
        max_ngram_to_include: Optional[int] = None,
        ngram_delimiter: str = ";",
        remove_delimiter: bool = False,
        verbose: bool = True,
    ) -> List[str]:
        """Preprocess the word list.

        Args:
            words (List[str]): List of words.
            sort (bool, optional): Sort the words. Defaults to True.
            lowercase (bool, optional): Convert the words to lowercase. Defaults to False.
            unique (bool, optional): Remove duplicate words. Defaults to True.
            remove_tag (bool, optional): Remove the tag from the words. Defaults to False.
            max_ngram_to_include (Optional[int], optional): Maximum ngram to include. Defaults to None.
            ngram_delimiter (str, optional): Delimiter for ngram. Defaults to ";".
            remove_delimiter (bool, optional): Remove the delimiter. Defaults to False.
            verbose (bool, optional): Show the progress. Defaults to True.

        Returns:
            List[str]: List of words.
        """
        if remove_delimiter:
            words = [word.replace(ngram_delimiter, "") for word in words]
        if max_ngram_to_include:
            words = [
                word
                for word in words
                if len(word.split(ngram_delimiter)) <= max_ngram_to_include
            ]

        if remove_tag:
            words = [word.split("/")[0] for word in words]
        words = [
            word.lower() if lowercase else word
            for word in words
            if not word.startswith("#")
        ]
        if unique:
            words = list(set(words))
            if verbose:
                logger.info(
                    "Remove duplicate words, No. of words: %s",
                    len(words),
                )
        if sort:
            words = sorted(words)
        return words

    @staticmethod
    def append_to_jsonl(
        data: dict,
        filename: str,
        encoding: str = "utf-8",
    ) -> None:
        """Append a json payload to the end of a jsonl file."""
        json_string = json.dumps(data, ensure_ascii=False)
        with open(filename, "a", encoding=encoding) as f:
            f.write(json_string + "\n")

    @staticmethod
    def load_jsonl(
        filename: str,
        encoding: str = "utf-8",
    ) -> List[dict]:
        """Load a jsonl file into a list of json objects."""
        with open(filename, "r", encoding=encoding) as f:
            return [json.loads(line) for line in f]

    @staticmethod
    def save_jsonl(
        data: List[dict],
        filename: str,
        encoding: str = "utf-8",
    ) -> None:
        """
        Save a list of json objects to a jsonl file.
        """
        with open(filename, "w", encoding=encoding) as f:
            for line in data:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")

    @staticmethod
    def remove_duplicates_from_list_of_dicts(
        data: List[dict],
        key: str,
    ) -> List[dict]:
        """Remove duplicates from a list of dicts based on a key."""
        seen = set()
        new_data = []
        for d in data:
            if d[key] not in seen:
                new_data.append(d)
                seen.add(d[key])
        return new_data
