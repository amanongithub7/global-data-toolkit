import unittest

from globalclimateanalysis.dataset import bycountry


class TestGenerator(unittest.TestCase):
    def test_exception_on_non_csv_file(self):
        self.assertRaises(ValueError, bycountry.Generator, "noncsv.pdf")
