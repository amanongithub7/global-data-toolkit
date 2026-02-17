# Global Climate Analysis (2000-2024) 🌍

This is a Python-based project that seeks to analyze global climate data between
2000 and 2024.

Refer to `dataset/README.md` for information about the
[dataset](https://www.openml.org/search?type=data&sort=qualities.NumberOfInstances&status=active&id=46731)
sourced from OpenML.

## Development 🧑‍💻

### Installing the Package in Editable Mode 💾

In order to import the `globalclimateanalysis` package in python scripts and
notebooks, or to run its unit tests, we need to make the module visible by these
processes by installing the package using `pip`:

```bash
pip install -e . # in the root dir of the repository
```

The `-e` flag indicates to pip that this is an editable package i.e. when
changes are made to the source code, they will be reflected in processes that
import the package.

## Testing 🧪

### Testing File Structure 🗂️

The unit tests for the `globalclimateanalysis` package are contained in
`tests/`, with tests for each subpackage in relevant folders within `tests`.

### Running Tests ▶️

In order to run all unit tests for the `globalclimateanalysis` package from the
`tests/` directory, run this command from the root of the repository:

```bash
python -m unittest discover tests -v
```

In order to run all unit tests for a specific subpackage such as `dataset`, run:

```bash
python -m unittest discover tests.dataset -v
```

In order to run a specific test file (which usually corresponds to a module of a
subpackage), run:

```bash
python -m unittest -v tests.dataset.test_csvfieldmap
```

```

```
