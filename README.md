# Flask HTMX app

An example of how to build a HTMX website with Flask.

## Development

To start the development envioronment start by running `make up` and it will sync or rebuild teh container automatically when changes are made to the codebase.

```sh
make up
```

The docker compose `--watch` flag watches for changes in the codebase and depending on what you do it either hot reloads or rebuilds the container.

For example if you add new dependencies or update javascript code in `static/js` folders it rebuilds the container. If you just change Python code or templates changes will be available without rebuilding the container.

## Install dependencies

### Python

Uses [uv](https://github.com/astral-sh/uv) for managing dependencies.

Add production dependencies to [requirements/prod.in](requirements/prod.in) and development dependencies to [requirements/dev.in](requirements/dev.in). Then run this command to compile the requirements to txt files used for installing all dependencies.

```sh
make pip-compile
```

### Node

Install node dependencies with npm.

```sh
npm install htmx.org
```

## Build Docker image

This script will build a docker image and reduce its size with [slim](https://github.com/slimtoolkit/slim).

```bash
./scripts/build-docker-image.sh
```
