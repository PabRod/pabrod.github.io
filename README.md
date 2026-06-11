# Workflow

## Install

- Clone me with `--recurse-submodules` option
- All dependencies are listed in a conda/poetry friendly way.
- The only exception is the `THEME`, that is managed as a submodule via `git`.
- Using `poetry` is recommended.

## Develop

While editing, you can see a live version of the website using:

```sh
poetry run make devserver
```

## Generate and publish

```sh
poetry run make github
```
