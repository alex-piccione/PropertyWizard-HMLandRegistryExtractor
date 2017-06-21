import unittest
import os

from src.extractor.filerRader import FileReader

DATA_FOLDER = "../data"
TEST_FILE = "example pp 15 rows.csv"
TEST_FILE_HEADERS = "example pp 15 rows with header.csv"

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


    def _getTestFilePath(self, file_name):

        # os.getcwd() can be wrong (depends on the settings of the test configuration)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        test_file = os.path.join(current_dir, DATA_FOLDER, file_name)
        return test_file