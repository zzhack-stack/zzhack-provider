# zzhack-provider
This repository is used to provide data to zzhack.

## TODO
- [x] publish post
- [ ] generate static assets from source code
- [x] analyze the relationship between posts and generate a root metadata file to describe the relationship

## Quick start
First you should install dependencies by `pipenv`

```bash
pipenv install
```

Run the follow commands in root of the project to link the `zzhack` CLI to global.
```bash
pipenv run setup
```

## Publish posts
Run `pipenv run zzhack publish` to publish the post which in current path, the command will create a metadata file that describe information of the post called `metadata.json`.
```json
{
    "cover": "str", "title": "str", "filename": "str", "sammary": "str"
}
```

The `metadata.json` file can help `zzhack` app to easies know more key information about posts.

## LICENSE
GPL.
