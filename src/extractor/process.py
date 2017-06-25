from extractor.logger import Logger
from extractor.fileReader import FileReader
from extractor.repositories.sellDataMongoRepository import SellDataMongoRepository

logger = Logger.create(__name__)

class Process():

    def __init__(self, file_reader: FileReader, raw_sell_data_repository: SellDataMongoRepository):

        self.file_reader = file_reader
        self.raw_data_repository = raw_sell_data_repository

    def run(self, csv_file: str):

        logger.info('Run.')

        # load file
        try:
            records = self.file_reader.read(csv_file, False)
            logger.info(f'Reader read {len(records)} records.')
        except Exception as error:
            return logger.fatal(f"Fail to parse CSV file. {error}")

        # save data
        try:
            for record in records:
                # if record.action == "a":
                self.raw_data_repository.save(record)
            logger.info(f'All record saved.')
        except Exception as error:
            return logger.fatal(f"Fail to save records. {error}")

        logger.info(f'Process end.')

