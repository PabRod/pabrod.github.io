# Workflow

## Install

- All dependencies are listed in a conda/poetry friendly way.
- The only exception is the `THEME`.
    - Clone it from [here](https://github.com/getpelican/pelican-themes).
    - Set path at `pelicanconf.py`

## Develop

While editing, you can see a live version of the website using:

```sh
pelican -r -l
# or
make devserver
```

## Generate and publish

```sh
make github
```