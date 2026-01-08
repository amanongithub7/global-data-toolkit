import unittest

from globalclimateanalysis.dataset import csvfieldmap


class TestConvertCsvFieldNameToSnakeCase(unittest.TestCase):
    def test_existing_field_conversion(self):
        snake_version = csvfieldmap.convert_csv_field_name_to_snake_case(
            "Forest Area (%)"
        )
        expected_snake_version = "forest_area_%"
        self.assertEqual(snake_version, expected_snake_version)


# if __name__ == "__main__":
#     unittest.main()
