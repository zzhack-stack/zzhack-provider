from typing import Final
from os import listdir, path
from .constants import METADATA_FILENAME
from json import loads, dumps
from pathlib import Path

"""
The purpose of the script is traverse all posts and analyze the relationship between them
and auto create a metadata file in CI(GitHub Action) that describe the relationship. And the
Rust WASM app will know the relationship between posts via just read the metadata file.

┌──────────────────────────────────────────────────┐
│                                                  │
│ metadata.json                                    │
│                                                  │
│ categories                                       │
│                                                  │
│      ┌─────────────────────────────────────┐     │
│      │                                     │     │
│      │ post.md                             │     │
│      │                                     │     │
│      │ metadata.json                       │     │
│      │                                     │     │
│      └─────────────────────────────────────┘     │
│                                                  │
│                                                  │
└──────────────────────────────────────────────────┘
"""

POSTS_PATH: Final = "./posts"

def extract_metadata_from_categories(category_name):
    posts = listdir(category_name)

    def map_filename2metadata(post_dirname):
        post_dir_or_file = Path(path.join(category_name, post_dirname))
        if not post_dir_or_file.is_dir():
            return None

        post_path = path.join(category_name, post_dirname, METADATA_FILENAME)
        metadata_file_handle = open(post_path, 'r')
        metadata_content = metadata_file_handle.read()
        metadata_dict = loads(metadata_content)
        metadata_file_handle.close()

        return metadata_dict

    return list(filter(lambda metadata: metadata != None, map(map_filename2metadata, posts)))

def analyze_metadata():
    dist_metadata = {
        'categories': {}
    }

    categories = listdir(POSTS_PATH)
    parsed_metadata = list(map(lambda category_name: extract_metadata_from_categories(path.join(POSTS_PATH, category_name)), categories))

    for idx, category in enumerate(categories):
        dist_metadata['categories'][category] = parsed_metadata[idx]
    
    # create root metadata, if the metadata.json is exists in root path, overwrite it without being asked
    file_handle = open(METADATA_FILENAME, 'w')
    file_handle.write(dumps(dist_metadata, ensure_ascii=False, indent=2))
    file_handle.close()
    print("Compolet create metadata.json in the root path！🎉")
