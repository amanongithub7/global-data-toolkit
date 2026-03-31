import logging
import os
import shutil

import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(filename="bycountry.log", level=logging.INFO)


class Generator:
    """Generates per-country csv files from combined data csv.

    Generates csv files for each country's records present in the csv data file, and stores intermittent variables such as
    the path of the csv file and a pandas' DataFrame containing the csv data.

    Attributes
    ----------
    data : pandas.DataFrame
        a DataFrame containing the unfiltered, raw csv data
    bycountry_data_dir : str
        the directory where generated per-country csv files should be stored, defaults to "./data/bycountry/" when a path is not provided upon class init
    Methods
    -------
    _files_already_exist() --> bool:
        returns True if csv files for countries in the main data csv seem to exist, and False otherwise.
    """

    bycountry_data_dir: str | os.PathLike
    countries: set[str]
    data: pd.DataFrame

    def __init__(
        self, csv_file_path: str, data_dir: str | os.PathLike = "./data"
    ) -> None:
        """Validate params and initialize Generator with a pandas.DataFrame and directory string.

        Initialize the Generator class once a few checks are performed:
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
            directory where the bycountry/ folder of csvs should be created, defaults to "./data".
        Raises
        ------
        ValueError
            if csv_file_path doesn't specify a .csv file.
        FileNotFoundError
            if the file indicated by csv_file_path doesn't exist, or the directory indicated by data_dir doesn't exist.
        """

        # if the file extension is not ".csv", a ValueError is raised since this module only accepts csv type files
        _, ext = os.path.splitext(csv_file_path)
        if ext != ".csv":
            raise ValueError(
                f"The provided file '{csv_file_path}' must be a '.csv' file path (absolute or relative)."
            )

        # if the file doesn't exist, terminate the program with a FileNotFoundError
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(
                f"The provided file '{csv_file_path}' does not exist."
            )

        self.data = pd.read_csv(csv_file_path)
        if "Country" in self.data:
            self.countries = set(self.data["Country"].unique())
        else:
            raise KeyError(
                "A 'Country' column is expected in the provided .csv file for generation of per-country files. Please make sure it exists."
            )

        if len(self.countries) <= 1:
            raise ValueError(
                "The provided csv file contains less than 2 countries. Generating per-country csvs is redundant."
            )

        # if the directory for storing per-country csv files doesn't exist,
        if not os.path.isdir(data_dir):
            # either create the directory if the client has chosen the default dir
            if data_dir == "./data":
                os.mkdir("./data")
            # or else raise a FileNotFoundError if the client has specified a non-existent dir
            else:
                raise FileNotFoundError(
                    f"The provided directory '{data_dir}' does not exist."
                )

        # note that this directory path is stored here, we don't create the directory (if it doesn't exist) ...
        # ... that is deferred to the generate_country_csv_files method
        self.bycountry_data_dir = os.path.join(os.path.abspath(data_dir), "bycountry")

    # TODO:
    def _files_already_exist(self) -> bool:
        """Check if per-country csvs already exist in the data_dir.

        Performs a shallow check to determine if number and names of csv files in the bycountry directory match
        number and names of countries in the main csv file.

        Note: this doesn't check the contents or lengths of the csv files.
        Returns
        -------
        True if {data_dir}/bycountry/ exists and contains exactly the same countries as in the main csv.
        False otherwise.
        """
        if not os.path.isdir(self.bycountry_data_dir):
            return False

        dir_files: list[str] = os.listdir(self.bycountry_data_dir)

        # 1. check if # of files in the bycountry/ dir = # of countries in csv file
        if len(dir_files) != len(self.countries):
            return False

        # remove file extension before comparison with set of countries
        csv_suffix = ".csv"
        countries_with_files: list[str] = []
        for file in dir_files:
            if file.lower().endswith(csv_suffix.lower()):
                countries_with_files.append(file[0 : -len(csv_suffix)])

        # 2. check if each country in the csv file is in the dbycountry/ dir
        for country in self.countries:
            if country not in countries_with_files:
                return False

        # 3. return True ("files already exist") if both conditions are met
        return True

    def _clean_storage(self):
        """Clean the per-country csv storage directory.

        Remove any files inside the directory.
        """

        if not os.path.isdir(self.bycountry_data_dir):
            return

        dir_files: list[str] = os.listdir(self.bycountry_data_dir)

        if len(dir_files) == 0:
            return
        else:
            for file in dir_files:
                file_path = os.path.join(self.bycountry_data_dir, file)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    logger.critical(
                        "Clean up during per-country file generation failed. Failed to delete %s. Reason: %s. \
                        Clear the %s folder and try again."
                        % (file, self.bycountry_data_dir, e)
                    )

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
