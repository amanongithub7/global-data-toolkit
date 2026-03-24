import os
import shutil
import tempfile
import unittest

from globalclimateanalysis.dataset import bycountry


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

    def test_succeeds_on_valid_csv_and_data_dir_args(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.dirname(os.path.abspath(__file__))
            test_csv_path = os.path.join(
                test_dir, "bycountry", "valid_csv_8_countries.csv"
            )
            shutil.copy(test_csv_path, tmpdir)
            os.chdir(tmpdir)

            os.mkdir("./existent_data_dir")

            _ = bycountry.Generator("valid_csv_8_countries.csv", "./existent_data_dir")
