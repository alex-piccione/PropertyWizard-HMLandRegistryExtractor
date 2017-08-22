import codecs
import csv
from datetime import datetime
from typing import List

from extractor.logger import Logger
from extractor.entities.saleRawData import SaleRawData

logger = Logger.create(__name__)

class FileReader():

    def __init__(self):

        self.errors = None
        self.records: List[SaleRawData] = None

    def read(self, file_, has_headers = False):
        """
        Parse the CSV file.

        :param file_: CSV file
        :param has_headers: first row contains fields names?
        :return: an array of SaleRawData
        """

        logger.info(f'Read file "{file_}"')

        self.errors = []
        self.records = []

        with codecs.open(file_, "rt") as csv_file:
            reader = csv.reader(csv_file)

            if has_headers:
                next(reader, None)

            for line in reader:
                try:
                    sale_data = self._parse_line(line)
                    self.records.append(sale_data)
                except Exception as exc:
                    self.errors.append(str(exc))

        logger.info(f'Read end. Records: {len(self.records)}.')

        return self.records


    def _parse_line(self, line):
        guid = line[0]
        price = float(line[1])
        date_ = self._parse_date(line[2])  # datetime.strptime(line[2], "%Y-%m-%d").date() # datetime parsing is so crappy that I prefer to do it myself.  [0:10]  # get yyyy-MM-dd
        postcode = line[3]
        property_type = line[4]
        yn = line[5]
        hold_type = line[6]

        paon = line[7]  # Primary Address Object Number
        saon = line[8]  # Secondary Address Object Number
        street = line[9]
        locality = line[10]
        city = line[11]
        district = line[12]
        county = line[13]

        x = line[14]
        action = line[15]  # Add, Change, Delete

        item = SaleRawData(guid, price, date_, postcode, property_type, yn, hold_type,
                           paon, saon, street, locality, city, district, county, x, action)

        return item

    def _parse_date(self, text):
        try:
            return datetime(int(text[0:4]), int(text[5:7]), int(text[8:10]))
        except:
            raise Exception(f'Fail to parse date. Text: "{text}".')
