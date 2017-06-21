import codecs
import csv
from datetime import date

from extractor.rawSellData import RawSellData


class FileReader():

    def __init__(self):

        self.errors = None
        self.result = None

    def read(self, file_, has_headers = False):
        print("read")
        self.errors = []
        self.result = []

        with codecs.open(file_, "rt") as csv_file:
            reader = csv.reader(csv_file)

            if has_headers:
                next(reader, None)

            for line in reader:
                try:
                    sell_data = self._parse_line(line)
                    self.result.append(sell_data)
                except Exception as exc:
                    self.errors.append(str(exc))

        return self.result

    def _parse_line(self, line):
        guid = line[0]
        price = float(line[1])
        date_ = self._parse_date(line[2])  #   datetime.strptime(line[2], "%Y-%m-%d").date() # datetime parsing is so crappy that I prefer to do it myself.  [0:10]  # get yyyy-MM-dd
        print(date)
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

        return RawSellData(guid, price, date_, postcode, property_type, yn, hold_type,
                           paon, saon, street, locality, city, district, county, x, action)

    def _parse_date(self, text):
        try:
            return date(int(text[0:4]), int(text[5:7]), int(text[8:10]))
        except:
            raise Exception("Fail to parse date. String: '{}'.".format(text))


if __name__ == "__main__":

    filename = "example pp 15 rows.csv"
    f = FileReader()
    f.read(filename)

    if f.errors and len(f.errors) > 0:
        print("Errors: {0}".format(len(f.errors)))
        for e in f.errors:
            print(e)
        exit(1)

    result = f.result
    for d in result:
        print("Guid: {guid}".format(guid = d.guid))

