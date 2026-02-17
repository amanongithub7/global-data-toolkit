import os


class Generator:
    """
    Generates csv files for each country's records present in the csv data file, and stores intermittent variables such as
    the path of the csv file and a pandas' DataFrame containing the csv data.

    ...
    Attributes
    ----------
    csv_file_path : str
        directory where original csv file containing climate records for different countries is present
    data_dir : str , optional
        the directory where generated per-country csv files can be stored, defaults to "./data"

    Methods
    -------
    _files_already_exist() --> bool:
        returns True if csv files for countries seem to exist, and False otherwise.
    """

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

    # TODO: clean method cleans files if they are incomplete/invalid
    # def clean(self) --> None:
