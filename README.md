# Global Data Toolkit 🌍

## Overview

`globaldatatoolkit` is a Python package that seeks to simplify the use of global
datasets for data analysis and machine learning applications.

Currently, it's main module is the `bycountry` module of the `dataset`
subpackage, which exposes a `DataLoader` interface for loading global datasets
as per-country `pandas.DataFrames` in runtime memory.

Refer to the [API Documentation](https://amanongithub7.github.io/global-data-toolkit/)
for more information about the available functionality.

Refer to `example_notebooks/__subpackage__/` for jupyter notebooks with sample
usage of different modules.

## Usage 📊

TODO

## Development 🧑‍💻

### Setting Up the Conda Environment 🐍

The Conda environment containing the Python version and required packages is
stored in `env.yml`. In order to replicate this environment, run either one of
these two commands in the command line:

if you want to keep the environment name global-data-toolkit:

```bash
 conda env create -f env.yml
```

or, if you want to set your own environment name:

```bash
 conda env create -f environment.yml -n new_env_name
```

### Installing the Package in Editable Mode 💾

In order to import the `globaldatatoolkit` package in python scripts, jupyter
notebooks, or to run its unit tests, we need to make the module visible to these
processes by installing the package using `pip`:

```bash
pip install -e . # in the root dir of the repository
```

The `-e` flag indicates to pip that this is an editable package i.e. when
changes are made to the source code, they will be reflected in processes that
import the package.

## Testing 🧪

### Unit Tests 🗂️

The unit tests for the `globaldatatoolkit` package are contained in `tests/`,
with tests for each subpackage in subpackage-named folders within `tests`.

#### Running Tests ▶️

In order to run all unit tests for the `globaldatatoolkit` package from the
`tests/` directory, run this command from the root of the repository:

```bash
python -m unittest discover tests -v
```

In order to run all unit tests for a specific subpackage such as
`globaldatatoolkit.dataloaders`, run:

```bash
python -m unittest discover tests.dataloaders -v
```

In order to run a specific test file (which usually corresponds to a module of a
subpackage), run:

```bash
python -m unittest -v tests.dataloaders.test_bycountry
```
