from pathlib import Path

import aiofiles

__all__ = ("save_file",)


def generate_file_name(file_name: str) -> str:
    """
    Generates a secure file name for the given file.
    """


async def save_file(file, path: Path) -> None:
    """
    Stores the file at the given file-path.
    """
    async with aiofiles.open(path, "w") as out:
        await out.write(file)
        await out.flush()
