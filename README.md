<img src="https://raw.githubusercontent.com/zzhack-stack/zzhack-provider/main/docs/Artboard.svg" />

# zzhack-provider
This repository is used to provide data to zzhack.

## Quick start
First you should install dependencies by `pipenv`

```bash
pipenv install
```

Run the follow commands in root of the project to link the `zzhack` CLI to global.
```bash
pipenv run setup
```

Run `pipenv run zzh --help` for more detail:
```shell
Usage: zzhack [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  analysis  Create root metadata.json
  publish   Generate corresponding metadata.json in current path
  upload    Upload the static files to CDN
```

## Publish posts
Run `pipenv run zzhack publish` to publish the post which in current path, the command will create a metadata file that describe information of the post called `metadata.json`.
```json
{
    "cover": "str", "title": "str", "filename": "str", "sammary": "str"
}
```

The `metadata.json` file can help `zzhack` app to easies know more key information about posts.

## Upload posts
When you created a PR on `zzhack-provider`, the GitHub Actions will help you to run `pipenv run zzhack upload`, the zzhack CLI will create a snapshot of current project and then upload to the CDN, the `zzhack` app will take these data which from the CDN as rendering resource.

So you don't have to do anything, if you wanna contribute some article to zzhack, just write down as a markdown file, and create a PR the `zzhack` CLI will do everything you don't care about. 

## Analysis
For easy `zzhack` app read these data for render on page, the `zzhack` CLI will analyze the directory structure of posts and generate a root matadata file for describe this replationship between posts.

Also you don't have to care about these things, the CLI will start analyze during the CI running, and commit the change of root meatdata automatically.

## LICENSE
GPL.
