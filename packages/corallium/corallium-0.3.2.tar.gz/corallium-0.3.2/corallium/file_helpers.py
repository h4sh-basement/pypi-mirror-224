"""File Helpers."""

import os
import shutil
import string
import time
import webbrowser
from contextlib import suppress
from functools import lru_cache
from pathlib import Path

from beartype import beartype
from beartype.typing import Any, Dict, List, Optional

from .log import logger
from .tomllib import tomllib

LOCK = Path('poetry.lock')
"""poetry.lock Path."""

PROJECT_TOML = Path('pyproject.toml')
"""pyproject.toml Path."""

COPIER_ANSWERS = Path('.copier-answers.yml')
"""Copier Answer file name."""

MKDOCS_CONFIG = Path('mkdocs.yml')
"""mkdocs.yml Path."""

# ----------------------------------------------------------------------------------------------------------------------
# Read General Text Files


@beartype
def read_lines(path_file: Path, encoding: Optional[str] = 'utf-8', errors: Optional[str] = None) -> List[str]:
    """Read a file and split on newlines for later parsing.

    Args:
        path_file: path to the file
        encoding: defaults to 'utf-8'
        encoding: defaults to None, Use 'ignore' if needed'

    Returns:
        List[str]: lines of text as list

    """
    return path_file.read_text(encoding=encoding, errors=errors).splitlines() if path_file.is_file() else []


@beartype
def tail_lines(path_file: Path, *, count: int) -> List[str]:
    """Tail a file for up to the last count (or full file) lines.

    Based on: https://stackoverflow.com/a/54278929

    > Tip: `file_size = fh.tell()` -or- `os.fstat(fh.fileno()).st_size` -or- return from `fh.seek(0, os.SEEK_END)`

    Args:
        path_file: path to the file
        count: maximum number of lines to return

    Returns:
        List[str]: lines of text as list

    """
    with path_file.open('rb') as f_h:
        rem_bytes = f_h.seek(0, os.SEEK_END)
        step_size = 1  # Initially set to 1 so that the last byte is read
        found_lines = 0
        while found_lines < count and rem_bytes >= step_size:
            rem_bytes = f_h.seek(-1 * step_size, os.SEEK_CUR)
            if f_h.read(1) == b'\n':
                found_lines += 1
            step_size = 2  # Increase so that repeats(read 1 / back 2)

        if rem_bytes < step_size:
            f_h.seek(0, os.SEEK_SET)
        return [line.rstrip('\r') for line in f_h.read().decode().split('\n')]


# ----------------------------------------------------------------------------------------------------------------------
# Read Specific File Types


@beartype
def find_in_parents(*, name: str, cwd: Optional[Path] = None) -> Path:
    """Recursively locate the path to the file in the current directory or parents."""
    msg = f'Could not locate {name} in {cwd} or in any parent directory'
    start_path = (cwd or Path()).resolve() / name
    try:
        while not start_path.is_file():
            start_path = start_path.parents[1] / name
    except IndexError:
        raise FileNotFoundError(msg) from None
    return start_path


@beartype
def get_tool_versions(cwd: Optional[Path] = None) -> Dict[str, List[str]]:
    """Parse a `.tool-versions` file."""
    tv_path = find_in_parents(name='.tool-versions', cwd=cwd)
    return {
        line.split(' ')[0]: line.split(' ')[1:]
        for line in tv_path.read_text().splitlines()
    }


@lru_cache(maxsize=5)
def read_pyproject(cwd: Optional[Path] = None) -> Any:
    """Read the 'pyproject.toml' file once."""
    toml_path = find_in_parents(name='pyproject.toml', cwd=cwd)
    try:
        pyproject_txt = toml_path.read_text(encoding='utf-8')
    except Exception as exc:
        msg = f'Could not locate: {toml_path}'
        raise RuntimeError(msg) from exc
    return tomllib.loads(pyproject_txt)  # pyright: ignore[reportGeneralTypeIssues]


@lru_cache(maxsize=5)
def read_package_name(cwd: Optional[Path] = None) -> str:
    """Read the package name once."""
    poetry_config = read_pyproject(cwd=cwd)
    return str(poetry_config['tool']['poetry']['name'])


@beartype
def read_yaml_file(path_yaml: Path) -> Any:
    """Attempt to read the specified yaml file. Returns an empty dictionary if not found or a parser error occurs.

    > Note: suppresses all tags in the YAML file

    Args:
        path_yaml: path to the yaml file

    Returns:
        dictionary representation of the source file

    """
    try:
        import yaml  # lazy-load the optional dependency
    except ImportError as exc:
        raise RuntimeError("The 'calcipy[docs]' extras are missing") from exc

    # PLANNED: Refactor so that unsafe_load isn't necessary:
    #   read_text; remove any line containing ': !!python'; then yaml.loag

    # Based on: https://github.com/yaml/pyyaml/issues/86#issuecomment-380252434
    yaml.add_multi_constructor('', lambda _loader, _suffix, _node: None)
    yaml.add_multi_constructor('!', lambda _loader, _suffix, _node: None)
    yaml.add_multi_constructor('!!', lambda _loader, _suffix, _node: None)
    try:
        return yaml.unsafe_load(path_yaml.read_text())  # nosemgrep
    except (FileNotFoundError, KeyError) as exc:  # pragma: no cover
        logger.warning('Unexpected read error', path_yaml=path_yaml, error=str(exc))
        return {}
    except yaml.constructor.ConstructorError:
        logger.exception('Warning: burying poorly handled yaml error')
        return {}


# ----------------------------------------------------------------------------------------------------------------------
# General

ALLOWED_CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + '-_.'
"""Default string of acceptable characters in a filename."""


@beartype
def sanitize_filename(filename: str, repl_char: str = '_', allowed_chars: str = ALLOWED_CHARS) -> str:
    """Replace all characters not in the `allow_chars` with `repl_char`.

    Args:
        filename: string filename (stem and suffix only)
        repl_char: replacement character. Default is `_`
        allowed_chars: all allowed characters. Default is `ALLOWED_CHARS`

    Returns:
        str: sanitized filename

    """
    return ''.join((char if char in allowed_chars else repl_char) for char in filename)


@beartype
def trim_trailing_whitespace(pth: Path) -> None:
    """Trim trailing whitespace from the specified file.

    PLANNED: handle carriage returns

    """
    line_break = '\n'
    stripped = [line.rstrip(' ') for line in pth.read_text().split(line_break)]
    pth.write_text(line_break.join(stripped))


# ----------------------------------------------------------------------------------------------------------------------
# Manage Files and Directories


@beartype
def if_found_unlink(path_file: Path) -> None:
    """Remove file if it exists. Function is intended to a doit action.

    Args:
        path_file: Path to file to remove

    """
    if path_file.is_file():
        logger.text('Deleting', path_file=path_file)
        path_file.unlink()


@beartype
def delete_old_files(dir_path: Path, *, ttl_seconds: int) -> None:
    """Delete old files within the specified directory.

    Args:
        dir_path: Path to directory to delete
        ttl_seconds: if last modified within this number of seconds, will not be deleted

    """
    for pth in dir_path.rglob('*'):
        if pth.is_file() and (time.time() - pth.stat().st_mtime) > ttl_seconds:
            pth.unlink()


@beartype
def delete_dir(dir_path: Path) -> None:
    """Delete the specified directory from a doit task.

    Args:
        dir_path: Path to directory to delete

    """
    if dir_path.is_dir():
        logger.text('Deleting', dir_path=dir_path)
        shutil.rmtree(dir_path)


@beartype
def ensure_dir(dir_path: Path) -> None:
    """Make sure that the specified dir_path exists and create any missing folders from a doit task.

    Args:
        dir_path: Path to directory that needs to exists

    """
    logger.text('Creating', dir_path=dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)


@beartype
def get_relative(full_path: Path, other_path: Path) -> Optional[Path]:
    """Try to return the relative path between the two paths. None if no match.

    Args:
        full_path: the full path to use
        other_path: the path that the full_path may be relative to

    Returns:
        relative path

    """
    with suppress(ValueError):
        return full_path.relative_to(other_path)
    return None


# ----------------------------------------------------------------------------------------------------------------------
# Open Files


@beartype
def open_in_browser(path_file: Path) -> None:  # pragma: no cover
    """Open the path in the default web browser.

    Args:
        path_file: Path to file

    """
    webbrowser.open(path_file.resolve().as_uri())
