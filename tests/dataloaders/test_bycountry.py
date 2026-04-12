import os
import shutil
import tempfile
import unittest
from collections.abc import Mapping

import pandas as pd

from globaldatatoolkit.dataloaders import bycountry


class TestGeneratorInit(unittest.TestCase):
    """Test cases for Generator's constructor method"""

    def test_raises_value_error_on_non_csv_type_file_arg(self):
        with self.assertRaises(ValueError) as cm:
            _ = bycountry.Generator("noncsv.pdf")

        caught_exception = cm.exception
        self.assertEqual(
            caught_exception.__str__(),
            "The provided file 'noncsv.pdf' must be a '.csv' file path (absolute or relative).",
        )

    def test_raises_file_not_found_error_on_nonexistent_csv_file_arg(self):
        with self.assertRaises(FileNotFoundError) as cm:
            _ = bycountry.Generator("nonexistent.csv")

        caught_exception = cm.exception
        self.assertEqual(
            caught_exception.__str__(),
            "The provided file 'nonexistent.csv' does not exist.",
        )

    def test_creates_data_folder_on_default_data_dir_arg(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy over the valid test csv file with arbitrary data
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)
            os.chdir(tmpdir)

            _ = bycountry.Generator("valid_csv_8_countries.csv")

            self.assertTrue(os.path.exists("./data"))

    def test_raises_key_error_on_absent_country_key(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_csv_path = os.path.join(tmpdir, "no_country_column.csv")
            with open(test_csv_path, "w") as f:
                f.write("col1,col2\n1,2")

            os.chdir(tmpdir)

            with self.assertRaises(KeyError) as cm:
                _ = bycountry.Generator("no_country_column.csv")

            exception = cm.exception
            self.assertIn(
                "A 'Country' column is expected in the provided .csv file for generation of per-country files. Please make sure it exists.",
                str(exception),
            )

    def test_raises_value_error_on_less_than_2_countries_in_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_csv_path = os.path.join(tmpdir, "one_country.csv")
            with open(test_csv_path, "w") as f:
                f.write("Country,Temperature\nIndia,41")

            os.chdir(tmpdir)

            with self.assertRaises(ValueError) as cm:
                _ = bycountry.Generator("one_country.csv")

            exception = cm.exception
            self.assertIn(
                "The provided csv file contains less than 2 countries. Generating per-country csvs is redundant.",
                str(exception),
            )

    def test_raises_file_not_found_error_on_nonexistent_data_dir_arg(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy over the valid test csv file with arbitrary data
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)
            os.chdir(tmpdir)

            # create a file named nonexisting, which should not be viewed as a dir by __init__
            file = open("nonexisting", "w")
            file.close()

            with self.assertRaises(FileNotFoundError) as cm:
                _ = bycountry.Generator("valid_csv_8_countries.csv", "./nonexisting")

            caught_exception = cm.exception
            self.assertEqual(
                caught_exception.__str__(),
                "The provided directory './nonexisting' does not exist.",
            )

    def test_success_and_default_dir_creation_on_no_data_dir_arg(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)
            os.chdir(tmpdir)

            _ = bycountry.Generator("valid_csv_8_countries.csv")

            self.assertTrue(os.path.isdir("./data"))

    def test_success_on_valid_csv_and_data_dir_args(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)
            os.chdir(tmpdir)

            os.mkdir("./existent_data_dir")

            _ = bycountry.Generator("valid_csv_8_countries.csv", "./existent_data_dir")


class TestGeneratorFilesAlreadyExist(unittest.TestCase):
    """Test cases for Generator class' _files_already_exist() method"""

    def test_returns_false_when_num_files_not_equal_to_num_countries(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            # default relative dir used by Generator to store per-country csv files
            os.mkdir("./data")

            os.mkdir("./data/bycountry")

            g = bycountry.Generator("valid_csv_8_countries.csv")

            self.assertFalse(g._files_already_exist())

    def test_returns_false_equal_num_files_countries_but_missing_country(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            # default relative dir used by Generator to store per-country csv files
            os.mkdir("./data")

            os.mkdir("./data/bycountry")

            # create 8 country csv files that don't match with the countries in the csv
            countries_with_files = {
                "Argentina",
                "Brazil",
                "China",
                "France",
                "India",
                "Palestine",
                "South Africa",
                "UK",
            }
            for country in countries_with_files:
                filepath = f"./data/bycountry/{country}.csv"
                with open(filepath, "w") as f:
                    f.write("header1,header2\n")
                    f.write("value1,value2\n")

            g = bycountry.Generator("valid_csv_8_countries.csv")

            self.assertFalse(g._files_already_exist())

    def test_returns_true_files_and_countries_matching(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            # default relative dir used by Generator to store per-country csv files
            os.mkdir("./data")

            os.mkdir("./data/bycountry")

            # create 8 country csv files that match with the countries in the csv
            countries_with_files = {
                "Argentina",
                "Australia",
                "China",
                "France",
                "Germany",
                "South Africa",
                "UK",
                "USA",
            }
            for country in countries_with_files:
                filepath = f"./data/bycountry/{country}.csv"
                with open(filepath, "w") as f:
                    f.write("header1,header2\n")
                    f.write("value1,value2\n")

            g = bycountry.Generator("valid_csv_8_countries.csv")

            self.assertTrue(g._files_already_exist())


class TestGeneratorCleanStorage(unittest.TestCase):
    """Test cases for the _clean_storage() method of the Generator class"""

    def test_deletes_all_files_from_bycountry_storage(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            os.mkdir("./data")
            os.mkdir("./data/bycountry")

            storage_files = ["Cambodia", "Ireland", "Senegal"]
            for file in storage_files:
                filepath = f"./data/bycountry/{file}.csv"
                with open(filepath, "w") as f:
                    f.write("header1,header2\n")
                    f.write("value1,value2\n")

            g = bycountry.Generator("valid_csv_8_countries.csv")
            g._clean_storage()

            dir_contents = os.listdir("./data/bycountry")
            self.assertTrue(len(dir_contents) == 0)

    def test_deletes_all_files_from_storage_custom_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            os.mkdir("./data_folder")
            os.mkdir("./data_folder/bycountry")

            storage_files = ["Cambodia", "Ireland", "Senegal"]
            for file in storage_files:
                filepath = f"./data_folder/bycountry/{file}.csv"
                with open(filepath, "w") as f:
                    f.write("header1,header2\n")
                    f.write("value1,value2\n")

            g = bycountry.Generator("valid_csv_8_countries.csv", "./data_folder")
            g._clean_storage()

            dir_contents = os.listdir("./data_folder/bycountry")
            self.assertTrue(len(dir_contents) == 0)


class TestGeneratorGenerate(unittest.TestCase):
    """Test cases for the generate method of bycountry.Generator"""

    def test_creates_dir_and_generates_csv_for_each_country_with_columns_preserved(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            tests_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                tests_dir, "bycountry", "valid_csv_8_countries.csv"
            )

            # copy test csv to current dir
            shutil.copy(test_csv_path, tmpdir)

            # change execution location to tmp dir
            os.chdir(tmpdir)

            # create data dir - the bycountry subdir doesn't exist and is expected to be created by the generate call
            os.mkdir("./data")

            # create Generator instance with default data dir
            g = bycountry.Generator("valid_csv_8_countries.csv")
            g.generate()

            # check that the bycountry data dir is generated by the generate call
            self.assertTrue(os.path.isdir("./data/bycountry"))

            bycountry_files = os.listdir("./data/bycountry")

            countries_in_csv = {
                "Argentina",
                "Australia",
                "China",
                "France",
                "Germany",
                "South Africa",
                "UK",
                "USA",
            }

            # check that each country in the csv has a file in the generated dir
            for file in bycountry_files:
                self.assertIn(file.removesuffix(".csv"), countries_in_csv)

            # finally, check that one of the files has the necessary columns transferred over (shallow test of data transfer)
            columns = [
                "Year",
                "Avg Temperature (°C)",
                "CO2 Emissions (Tons/Capita)",
                "Sea Level Rise (mm)",
                "Rainfall (mm)",
                "Population",
                "Renewable Energy (%)",
                "Extreme Weather Events",
                "Forest Area (%)",
            ]

            uk_df = pd.read_csv("./data/bycountry/UK.csv")
            for column in columns:
                self.assertTrue(column in uk_df)

    def test_prints_info_message_if_files_already_exist(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tests_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                tests_dir, "bycountry", "valid_csv_8_countries.csv"
            )

            # copy test csv to current dir
            shutil.copy(test_csv_path, tmpdir)

            # change execution location to tmp dir
            os.chdir(tmpdir)

            # create data dir
            os.mkdir("./data")
            os.mkdir("./data/bycountry")

            # create 8 country csv files that match with the countries in the csv
            countries_with_files = {
                "Argentina",
                "Australia",
                "China",
                "France",
                "Germany",
                "South Africa",
                "UK",
                "USA",
            }
            for country in countries_with_files:
                filepath = f"./data/bycountry/{country}.csv"
                with open(filepath, "w") as f:
                    f.write("header1,header2\n")
                    f.write("value1,value2\n")

            # create Generator instance with default data dir
            g = bycountry.Generator("valid_csv_8_countries.csv")

            with self.assertLogs(
                "globaldatatoolkit.dataloaders.bycountry", "INFO"
            ) as cm:
                g.generate()

            self.assertTrue(
                "INFO:globaldatatoolkit.dataloaders.bycountry:Generated files already exist in"
                in cm.output[0]
            )

            self.assertTrue(
                "/data/bycountry and are ready to be Loaded. Run Generator's `_clean_storage` method if clean up is required."
                in cm.output[0]
            )


class TestDataLoader(unittest.TestCase):
    def test_loads_correct_shape_data_with_custom_storage_dir(self):
        expected_data_lengths: Mapping[str, int] = {
            "Argentina": 2,
            "Australia": 1,
            "China": 1,
            "France": 1,
            "Germany": 1,
            "South Africa": 1,
            "UK": 2,
            "USA": 1,
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            tests_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                tests_dir, "bycountry", "valid_csv_8_countries.csv"
            )

            shutil.copy(test_csv_path, tmpdir)

            os.chdir(tmpdir)

            os.mkdir("custom_storage_dir")

            dl = bycountry.DataLoader("valid_csv_8_countries.csv", "custom_storage_dir")
            loaded_data = dl.load()

            for country_name, country_df in loaded_data.items():
                self.assertEqual(expected_data_lengths[country_name], len(country_df))
