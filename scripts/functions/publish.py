from bullet import SlidePrompt, Input, YesNo, colors
from os import listdir, path
from typing import Final, Union
from json import dumps
from pathlib import Path
from .constants import METADATA_FILENAME, POST_EXTENSION

SAMMARY_CHAR_COUNT: Final = 200

is_post_file = lambda extension: extension == POST_EXTENSION

def get_metadata_data_from_prompt(post_filename: str, content: str) -> dict[str, str]:
    post_title = Input(f"Please enter the title of {post_filename}: ").launch()
    is_set_cover = YesNo('Do you wanna set a cover for this post?').launch()
    sammary = content[:SAMMARY_CHAR_COUNT]
    base_metadata = {
        'title': post_title,
        'filename': post_filename,
        'sammary': sammary
    }

    if not is_set_cover:
        return base_metadata

    cover = Input("Please enter a link of the cover which you wanna set: ").launch()

    return {
        'cover': cover,
        **base_metadata
    }
    

def peek_post_filename():
    files = listdir('.')
    
    for file in files:
        filename, extension = path.splitext(file)
        
        if is_post_file(extension):
            return file
        
    raise Exception("Cannot find any post file in the current path, please check the path and try again.")

def read_post_content(filename: str):
    file_handle = open(filename, 'r')
    # read content by once
    all_content = file_handle.read()
    file_handle.close()

    return all_content

def create_post_metadata(data: Union[str, str]):
    file_path = Path(METADATA_FILENAME)

    if file_path.exists():
        is_overwrite = YesNo("We detects that the `metadata.json` is already exists, do you wanna overwrite it?", word_color = colors.foreground["yellow"]).launch()

        if not is_overwrite:
            return

    file_handle = open(METADATA_FILENAME, 'w')
    data['sammary'] = data['sammary'].replace('\n', '')
    metadata_data = dumps(data, ensure_ascii=False, indent=2)
    file_handle.write(metadata_data)
    file_handle.close()

def publish_post():
    """publish the markdown file as post"""
    post_filename = peek_post_filename()
    content = read_post_content(post_filename)
    post_metadata = get_metadata_data_from_prompt(post_filename, content)
    create_post_metadata(post_metadata)

def publish_book():
    """publish the directory as book"""
    pass

def publish_translate_post():
    """publish the markdown file as translate post"""
    pass
