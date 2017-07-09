import sys

from extractor.logger import Logger
from extractor.process import Process
from extractor.fileReader import FileReader
from extractor.repositories.saleRawDataMongoRepository import SaleRawDataMongoRepository
from extractor import config

logger = Logger.create(__name__)

def run(csv_file: str):
    logger.info(f"Run. CSV file: {csv_file}")

    file_reader = FileReader()
    connection_string = config.mongo_connection_string
    database_name = config.mongo_database_name
    sale_data_repository = SaleRawDataMongoRepository(connection_string, database_name)

    process = Process(file_reader, sale_data_repository)

    try:
        process.run(csv_file)
    except Exception as error:
        logger.fatal(f'Fail to run process on CSV file "{csv_file}". {error}')


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("No arguments no work to do")
        sys.exit(1)

    file_ = sys.argv[1]

    import os
    if not os.path.exists(file_):
        file_ = os.path.join(os.getcwd(), file_)
        if not os.path.exists(file_):
            print(f'File not found: "{file_}".')
            sys.exit(1)

    run(file_)



