from extractor.logger import Logger
from extractor.fileReader import FileReader
from extractor.repositories.sellDataMongoRepository import SellDataMongoRepository

logger = Logger.create(__name__)

class Process():

    def __init__(self, file_reader: FileReader, raw_sell_data_repository: SellDataMongoRepository):

        self.file_reader = file_reader
        self.raw_data_repository = raw_sell_data_repository

    def run(self, csv_file: str):

        records = None

        # load file
        try:
            records = self.file_reader.read(csv_file, False)
        except Exception as error:
            return logger.fatal(f"Fail to parse CSV file. {error}")

        # save data
        try:
            for record in records:
                # if record.action == "a":
                self.raw_data_repository.save(record)
        except Exception as error:
            return logger.fatal(f"Fail to save records. {error}")


