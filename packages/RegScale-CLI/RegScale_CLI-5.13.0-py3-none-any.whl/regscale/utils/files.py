"""Provide functions for dealing with files."""

import os
from pathlib import Path
from typing import Union


def print_file_contents(file_path: Union[str, Path]):
    """Print a file's contents to the console.
    :param file_path: a string or Path object
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if file_path.is_file():
        print(f'File "{file_path}" found!')
        print(file_path.read_text(encoding="utf-8"))


def print_current_directory(print_yaml=False):
    """Print the contents of the current directory and its path
    :param bool print_yaml: should the contents of the yaml file be printed?
    """
    current_dir = os.getcwd()
    print(f"Current Working Directory: {current_dir}")
    if print_yaml:
        init_file = os.path.join(current_dir, "init.yaml")
        print_file_contents(init_file)
