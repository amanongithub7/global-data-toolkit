import os

import pandas as pd


class Generator:
    """Generates per-country csv files from combined data csv.

    Generates csv files for each country's records present in the csv data file, and stores intermittent variables such as
    the path of the csv file and a pandas' DataFrame containing the csv data.

    Attributes
    ----------
    data : pandas.DataFrame
        a DataFrame containing the unfiltered, raw csv data
    data_dir : str , optional
        the directory where generated per-country csv files should be stored, defaults to "./data"
    Methods
    -------
    _files_already_exist() --> bool:
        returns True if csv files for countries in the main data csv seem to exist, and False otherwise.
    """

    data: pd.DataFrame
    data_dir: str

    def __init__(self, csv_file_path: str, data_dir: str = "./data") -> None:
        """Validate params and initialize Generator with a pandas.DataFrame and directory string.
        Initialize the Generator class once a few checks are done:
            1. param csv_file_path represents a csv file
            2. csv_file_path exists
            3. data_dir exists

        Upon validation, self.data is populated with a pandas.DataFrame version of the csv, and
        an absolute path for self.data_dir for storage of per-country csv files.

        Parameters
        ----------
        csv_file_path: str
            path of the main csv file with climate data of different countries.
        data_dir: str, optional
            directory where the bycountry/ folder of csvs should be stored, defaults to "./data".
        Raises
        ------
        ValueError
            if csv_file_path doesn't specify a .csv file.
        FileNotFoundError
            if the file indicated by csv_file_path doesn't exist, or the directory indicated by data_dir doesn't exist.
        """
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
    def _files_already_exist(self, countries: set) -> bool:
        """Check if per-country csvs already exist in the data_dir.

        Parameters
        ----------
        countries: set
            countries to verify files stored in {data_dir}/bycountry/ against.
        Returns
        -------
        True if {data_dir}/bycountry/ exists and contains exactly the same countries as in the main csv.
        False otherwise.
        """
        return False

    def generate(self):
        """Generate per country CSV files, if they don't already exist. Store them in {data_dir}/bycountry/."""

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
