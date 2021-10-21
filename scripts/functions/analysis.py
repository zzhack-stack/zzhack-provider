from typing import Final

# The purpose of the script is traverse all posts and analyze the relationship between them
# and auto create a metadata file in CI(GitHub Action) that describe the relationship. And the
# Rust WASM app will know the relationship between posts via just read the metadata file.

POSTS_PATH: Final = "./posts"
