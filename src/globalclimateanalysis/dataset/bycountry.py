import os

import pandas as pd


class Generator:
    """
    Generates csv files for each country's records present in the csv data file, and stores intermittent variables such as
    the path of the csv file and a pandas' DataFrame containing the csv data.

    ...
    Attributes
    ----------
    data : pandas.DataFrame
        a DataFrame containing the unfiltered, raw csv data
    data_dir : str , optional
        the directory where generated per-country csv files should be stored, defaults to "./data"
    Methods
    -------
    _files_already_exist() --> bool:
        returns True if csv files for countries seem to exist, and False otherwise.
    """

    data: pd.DataFrame
    data_dir: str

    def __init__(self, csv_file_path: str, data_dir: str = "./data") -> None:
        # if the file extension is not ".csv", raise a ValueError
        _, ext = os.path.splitext(csv_file_path)
        if ext != ".csv":
            raise ValueError(
                f"The provided file '{csv_file_path}' must be a '.csv' file path (absolute or relative)."
            )

        # if the file doesn't exist, `open()` raises a FileNotFoundError
        # NOTE: open() accepts both relative and absolute file paths
        _ = open(csv_file_path)

        # load csv data into a pandas.DataFrame object
        self.data = pd.read_csv(csv_file_path)

        # first check if dir exists
        self.data_dir = data_dir

    # TODO:
    def _files_already_exist(self) -> bool:
        """
        Check if per country csvs already exist.

        Returns:
            `True` if csvs' dir exists and # of csvs match # of countries in dataset and `False` otherwise

        Raises:
            `
        """
        return False

    def generate(self):
        """
        Generate per country CSV files, if they don't already exist. Store them in {data_dir}/by_country/.

        Raises:
        """

        # to get all unique values (countries) from a df in a numpyr array
        # unique_B = df['B'].unique()

        # check if any files exist in {data_dir}/by_country/ or if dir itself exists
        # if files exist but # of files != # of unique countries, call clean method to clean the by_country/ dir
        # otherwise create by_country/ dir if it doesn't exist

        # for each country in countries,
        # get subset DF for the country
        #   to generate sub-set of DF based on a column value:
        #   https://stackoverflow.com/questions/51004029/create-a-new-dataframe-based-on-rows-with-a-certain-value#51004086

        # save DF as csv file in {data_dir}/by_country/ with name *country*.csv

    # TODO: clean method cleans files if they are incomplete/invalid
    # def clean(self) --> None:
