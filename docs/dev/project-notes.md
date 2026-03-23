# Project: Global Climate Analysis (2000-2024)

Rough program notes for this project.

## `globalclimateanalysis`

### `dataset`

The `dataset` subpackage of `globalclimateanalysis` contains the following
modules:

#### `csvfieldmap`

- converts original csv data file's column names into snake_case for programming
  convenience

#### `bycountry`

##### `class Generator`

`__init__` params:

1. csv_file_path : str (no default)
2. data_dir : str (default="./data") -> assumes that the client is running in
   the root directory of the project

- generates csv files for each country's datapoints
  - checks for existing country csv files (shallow check - # of countries in csv
    = # of country csv files)
- prints stats at the end of generation
- dir for storing generated files -> provided by user otherwise
  `~/dataset/gca2000-2024/`

  ###### `generate()` method
  - Responsible for generating per-country csv files

  Logic:
  1. checks if files already exist (using other method). if they do, return
     true.
  2. use class' pd DataFrame - loop through and make dataframes for each country
  3. export dataframes into csvs and store in {data_dir}/by_country/ dir. Return
     true.

###### Tests

- make sure test for the column headings in generated `bycountry/` csvs -> they
  must be all headings in original csv except for "country"

##### `class Loader`

- `get_countries()` method that returns list of countries
- `load()` method that loads csvs into dataframes and returns dict of
  `country (str)` -> `country_records (pandas.DataFrame)`
  - optional `countries` str[] argument to load subset of countries
- if files don't exist?

##### Facade: `class DataLoader`

- facade for `Generator` and `Loader` classes
- `load` method returns dict of dataframes
- `__init__` constructor:
  - initializes a Generator with arg data_path
  - calls `generate` method of Generator to generate csv by country
  - initializes a Loader with arg `data_path` - (csv ext) - represents dir
    containing per country csv
- `__init__` parameters:

1. `data_dir` passed to `Generator()`

- `load()` method of `DataLoader`
  - `self.loader.load()` method loads csv files into program runtime memory in a
    dict of dataframes
  - returns the dict of pandas dataframes to client
- visualizer and other clients can use the data as they wish...
