from json import dumps, loads
import requests
from scripts.functions.utils import traverse_posts
from .constants import ISSUE_ID_KEY
# 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


def post_issue(title: str, addr: str, ak: str):
    res = requests.post(
        "https://api.github.com/repos/zzhack-stack/zzhack-provider/issues",
         headers={
            "Authorization": f"token {ak}"
        },
        json={
            "title": title, 
            "body": f"This issue is used to provide data for reply list, ref post lnk: {addr} "
        }
    )
    res = loads(res.text)

    return res["number"]

def create_issue(ak: str):    
    traverse_posts(handle_traverse_posts(ak))

def handle_traverse_posts(ak: str):
    def process_metadata(metadata, category_name, filename, metadata_path):
        has_create_issue = ISSUE_ID_KEY in metadata
        post_addr = f"https://www.zzhack.fun/{category_name}/posts/{filename}.md"

        if not has_create_issue:
            issue_id = post_issue(metadata["title"], post_addr, ak)
            metadata[ISSUE_ID_KEY] = issue_id
            metadata_data = dumps(metadata, ensure_ascii=False, indent=2)
            metadata_handle = open(metadata_path, "w")
            metadata_handle.write(metadata_data)
            metadata_handle.close()


    return process_metadata
