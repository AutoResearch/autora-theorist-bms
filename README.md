# AutoRA BMS Theorist

`autora-theorist-bms` is a Python module built on AutoRA that can be used to discover equations that fit data.

Website: [https://autoresearch.github.io/autora/](https://autoresearch.github.io/autora/)

## User Guide

You will need:

- `python` 3.8 or greater: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Install BMS as part of the `autora` package:

```shell
pip install -U "autora[theorist-bms]" --pre
```

> It is recommended to use a `python` environment manager like `virtualenv`.

Check your installation by running:
```shell
python -c "from autora.theorist.bms import BMSRegressor; BMSRegressor()"
```

## Developer Guide

### Get started

Clone the repository (e.g. using [GitHub desktop](https://desktop.github.com), 
or the [`gh` command line tool](https://cli.github.com)) 
and install it in "editable" mode in an isolated `python` environment, (e.g. 
with 
[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)) as follows:

In the repository root, create a new virtual environment:
```shell
virtualenv venv
```

Activate it:
```shell
source venv/bin/activate
```

Use `pip install` to install the current project (`"."`) in editable mode (`-e`) with dev-dependencies (`[dev]`):
```shell
pip install -e ".[dev]"
```

Run the test cases:
```shell
pytest tests/ --doctest-modules src/
```

Activate the pre-commit hooks:
```shell
pre-commit install
```

### Add new dependencies 

In pyproject.toml add the new dependencies under `dependencies`

Install the added dependencies
```shell
pip install -e ".[dev]"
```

### Publish the package

Update the metadata under `project` in the pyproject.toml file to include name, description, author-name, author-email and version

- Follow the guide here: [https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

Build the package using:
```shell
python -m build
```

Publish the package to PyPI using `twine`:
```shell
twine upload dist/*
```
