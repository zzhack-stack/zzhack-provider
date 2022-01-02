from scripts.functions.utils import traverse_posts
from json import loads, dumps
from time import time
from os import path

def handle_traverse_posts(metadata_content, category_name, post_name, current_path, metadata_path):
    post_path = path.join(current_path, post_name)
    post_file_handle = open(f'{post_path}.md', 'r')
    post_content = post_file_handle.read()
    post_file_handle.close()
    # update metadata info   
    if "content" in metadata_content and metadata_content['content'] == post_content:
        return

    metadata_content['summary'] = post_content[:200]
    metadata_content['content'] = post_content
    metadata_content['update_at'] = int(round(time() * 1000))
    serialize_metadata = dumps(metadata_content, ensure_ascii=False, indent=2)
    metadata_handle = open(metadata_path, 'w')
    metadata_handle.write(serialize_metadata)
    metadata_handle.close()

    
    

def update_posts():
    traverse_posts(handle_traverse_posts)
