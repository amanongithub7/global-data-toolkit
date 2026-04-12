import unittest

from globaldatatoolkit.dataloaders import csvfieldmap


class TestConvertCsvFieldNameToSnakeCase(unittest.TestCase):
    def test_existing_field_conversion(self):
        func_snake_version = csvfieldmap.convert_csv_field_name_to_snake_case(
            "Forest Area (%)"
        )
        expected_snake_version = "forest_area_%"
        self.assertEqual(func_snake_version, expected_snake_version)

    def test_exception_on_unknown_field_conversion(self):
        self.assertRaises(
            KeyError,
            csvfieldmap.convert_csv_field_name_to_snake_case,
            # a field that doesn't exist in the dataset
            "Cropland (%)",
        )
