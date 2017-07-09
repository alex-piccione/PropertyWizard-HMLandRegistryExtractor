from extractor.logger import Logger
from extractor.fileReader import FileReader
from extractor.repositories.saleRawDataMongoRepository import SaleRawDataMongoRepository
from extractor.saleDataProcessor import SaleDataProcessor


logger = Logger.create(__name__)

class Process():

    def __init__(self, file_reader: FileReader, sale_raw_data_repository: SaleRawDataMongoRepository, sale_data_processor: SaleDataProcessor):

        self.file_reader = file_reader
        self.raw_data_repository = sale_raw_data_repository
        self.data_processor = sale_data_processor

    def run(self, csv_file: str):

        logger.info('Run.')

        # load file
        try:
            records = self.file_reader.read(csv_file, has_headers=False)
            logger.info(f'Reader read {len(records)} records.')
        except Exception as error:
            return logger.fatal(f"Fail to parse CSV file. {error}")

        # save raw data
        new_records = []
        try:
            for record in records:
                # if record.action == "a":
                id_ = self.raw_data_repository.save(record)
                new_records.append(id_)
            logger.info(f'All records saved.')
        except Exception as error:
            return logger.fatal(f"Fail to save records. {error}")

        # elaborate the raw data
        #self.data_processor.process_new_records(new_records)

        logger.info(f'Process end.')

