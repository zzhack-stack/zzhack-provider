from json import loads
from typing import Callable, Any
from .constants import POSTS_DIRNAME, METADATA_FILENAME
from os import listdir
from pathlib import Path
from os import path

def traverse_posts(fn: Callable[[str, str, str, str], Any]):
    categories = listdir(POSTS_DIRNAME)

    for category_name in categories:
        current_path = Path(path.join(POSTS_DIRNAME, category_name))

        if not current_path.is_dir():
            continue

        traverse_post(current_path, fn, category_name)
        
def traverse_post(category_path: str, fn: Callable[[str, str, str, str], Any], category_name: str):
    posts = listdir(category_path)

    for post in posts:
        current_path = Path(path.join(category_path, post))

        if not current_path.is_dir():
            continue

        metadata_path = path.join(current_path, METADATA_FILENAME)
        metadata_handle = open(metadata_path)
        metadata_content = metadata_handle.read()
        metadata_handle.close()

        fn(loads(metadata_content), category_name, post, current_path, metadata_path)
