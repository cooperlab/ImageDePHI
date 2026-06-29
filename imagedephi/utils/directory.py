from collections.abc import Generator
from pathlib import Path


def iter_image_dirs(paths: list[Path], recursive: bool = False) -> Generator[Path, None, None]:
    for path in paths:
        if path.is_file():
            yield from iter_image_files(path)
        elif path.is_dir() and recursive:
            yield from iter_image_dirs(sorted(path.iterdir()), recursive)
        elif path.is_dir() and not recursive:
            for child in path.iterdir():
                if child.is_file():
                    yield from iter_image_files(child)
