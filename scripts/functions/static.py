from typing import Final, Callable
from os import listdir, path
from pathlib import Path
from .constants import CONSTANT_FILE_PATH, BUCKET_NAME, METADATA_FILENAME, POSTS_DIRNAME, POST_EXTENSION, CDN_DOMAIN
from qiniu import Auth, put_file, etag, CdnManager
import qiniu.config

"""
Generate static assets according current data in the project,
then dispatch the assets to CDN
"""

def upload_to_cdn(ak: str, sk: str):
    upload_constants(ak, sk)
    upload_metadata_and_posts(ak, sk)

def upload_stuff(file_path: str, ak: str, sk: str ):
    client = Auth(ak, sk)
    token = client.upload_token(BUCKET_NAME, file_path)
    res, info = put_file(token, file_path, file_path, version='v2')
    url = f"http://{CDN_DOMAIN}/{file_path}"
    cdn_manager = CdnManager(client)

    # prefetch source to nodes of CDN
    cdn_manager.prefetch_urls([url])

    print(f"Upload {file_path} successful! Ready to be access 🎉")
    print(f"And refresh {url}")

    assert res['key'] == file_path
    assert res['hash'] == etag(file_path)


def upload_constants(ak: str, sk: str):
    constants = listdir(CONSTANT_FILE_PATH)
    for constant_file in constants:
        file_path = path.join(CONSTANT_FILE_PATH, constant_file)
        upload_stuff(file_path, ak, sk)

def dir_filter(pre_path: str, l: list[str]):
    return filter(lambda file: Path(path.join(pre_path, file)).is_dir(), l)

def upload_post(pre_path: str, dirname: str, upload: Callable[[str], str]):
    for file in listdir(pre_path):
        filename, extension = path.splitext(file)
        filename_with_path = lambda filename: path.join(pre_path, filename)

        # is post file
        if extension == POST_EXTENSION:
            upload(filename_with_path(file))
        # is metadata file
        elif file == METADATA_FILENAME:
            upload(filename_with_path(METADATA_FILENAME))


def upload_metadata_and_posts(ak: str, sk: str):
    # upload posts
    categories = listdir(POSTS_DIRNAME)
    upload = lambda filename: upload_stuff(filename, ak, sk) 

    # upload root metadata
    upload(METADATA_FILENAME)

    for category in dir_filter(POSTS_DIRNAME, categories):
        post_path = path.join(POSTS_DIRNAME, category)

        # upload post metadata
        files = listdir(post_path)
        
        for file in dir_filter(post_path, files):
            upload_post(path.join(post_path, file), file, upload)
        


def gen_static():
    """Generate existing posts into static files that are easy to store in cloud"""
        
