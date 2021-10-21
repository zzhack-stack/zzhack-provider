from click import group, CommandCollection
from typing import Final
from scripts.functions import publish_post

@group()
def publish_group():
    pass

@group()
def static_group():
    pass

@group()
def analysis_group():
    pass

@publish_group.command()
def publish():
    publish_post()


cli: Final = CommandCollection(sources=[publish_group, static_group, analysis_group])

# def main():
cli()
