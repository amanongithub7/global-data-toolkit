import os
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
            # set up an existing.csv file with arbitrary data
            test_csv_path = os.path.join(tmpdir, "existing.csv")
            with open(test_csv_path, "w") as f:
                f.write("col1,col2\n1,2")

            os.chdir(tmpdir)

            _ = bycountry.Generator("existing.csv")

            self.assertTrue(os.path.exists("./data"))

    def test_raises_file_not_found_error_on_nonexistent_data_dir_arg(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # set up an existing.csv file with arbitrary data
            test_csv_path = os.path.join(tmpdir, "existing.csv")
            with open(test_csv_path, "w") as f:
                f.write("col1,col2\n1,2")

            os.chdir(tmpdir)
            # create a file named nonexisting, which should not be viewed as a dir by __init__
            file = open("nonexisting", "w")
            file.close()

            with self.assertRaises(FileNotFoundError) as cm:
                _ = bycountry.Generator("existing.csv", "./nonexisting")

            caught_exception = cm.exception
            self.assertEqual(
                caught_exception.__str__(),
                "The provided directory './nonexisting' does not exist.",
            )

    def test_succeeds_on_valid_csv_and_data_dir_args(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # set up an existing.csv file with arbitrary data
            test_csv_path = os.path.join(tmpdir, "existing.csv")
            with open(test_csv_path, "w") as f:
                f.write("col1,col2\n1,2")

            os.chdir(tmpdir)
            os.mkdir("./existent_data_dir")

            _ = bycountry.Generator("existing.csv", "./existent_data_dir")
