from click import group, CommandCollection, option
from typing import Final
from scripts.functions import publish_post, upload_to_cdn, analyze_metadata

@group()
def publish_group():
    pass

@group()
def static_group():
    pass

@group()
def analysis_group():
    pass

@publish_group.command(help="Generate corresponding metadata.json in current path")
def publish():
    publish_post()

@static_group.command(help="Upload the static files to CDN")
@option("--ak", required=True, help="The access key of QiNiu")
@option("--sk", required=True, help="The secret key of QiNiu")
def upload(ak: str, sk: str):
    upload_to_cdn(ak, sk)

@analysis_group.command(help="Create root metadata.json")
def analysis():
    analyze_metadata()

cli: Final = CommandCollection(sources=[publish_group, static_group, analysis_group])

def main():
    cli()
