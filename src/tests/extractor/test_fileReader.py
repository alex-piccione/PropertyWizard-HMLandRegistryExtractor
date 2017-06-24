import unittest
import os
from datetime import date

from src.extractor.filerRader import FileReader

DATA_FOLDER = "../data"
TEST_FILE = "example pp 15 rows.csv"
TEST_FILE_HEADERS = "example pp 15 rows with header.csv"
TEST_FILE_ONE_LINE = "example pp 1 row.csv"

class fileReaderTest(unittest.TestCase):

    def test_read_when_file_has_headers(self):
        file_ = self._getTestFilePath(TEST_FILE_HEADERS)

        # execute
        reader = FileReader()
        reader.read(file_, True) # has headers

        data = reader.result

        assert data is not None
        self.assertEqual(15, len(data), "size of result (records number)")
        assert len(data) == 15

    def test_read_when_file_has_not_headers(self):

        file_ = self._getTestFilePath(TEST_FILE)

        # execute
        reader = FileReader()
        reader.read(file_)

        data = reader.result

        assert data is not None
        self.assertEqual(15, len(data), "size of result (records number)")
        assert len(data) == 15

    def test_read__should__return_the_expected_RawPriceData_object(self):

        file_ = self._getTestFilePath(TEST_FILE_ONE_LINE)

        # execute
        reader = FileReader()
        reader.read(file_)

        data = reader.result

        expected_date = date(2002, 5, 31)

        record = data[0]
        self.assertEqual("{4E95D757-1CA7-EDA1-E050-A8C0630539E2}", record.transaction_id, "transaction_id")
        self.assertEqual(970000, record.price, "price")
        self.assertEqual(expected_date, record.date, "date")
        self.assertEqual("SW3 2BZ", record.post_code, "post_code")
        self.assertEqual("F", record.property_type, "property_type")
        self.assertEqual("N", record.yn, "yn")
        self.assertEqual("L", record.holding_Type, "holding_Type")

        self.assertEqual("paon", record.paon, "paon")
        self.assertEqual("saon", record.saon, "saon")
        self.assertEqual("street", record.street, "street")
        self.assertEqual("locality", record.locality, "locality")
        self.assertEqual("city", record.city, "city")
        self.assertEqual("district", record.district, "district")
        self.assertEqual("county", record.county, "county")

        self.assertEqual("x", record.x, "x")
        self.assertEqual("action", record.action, "action")


    def _getTestFilePath(self, file_name):

        # os.getcwd() can be wrong (depends on the settings of the test configuration)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        test_file = os.path.join(current_dir, DATA_FOLDER, file_name)
        return test_file