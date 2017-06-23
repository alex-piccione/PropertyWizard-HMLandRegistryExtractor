from pymongo import MongoClient

from extractor.repository import logger, \
    HM_PRICE_DATA_RAW_EXTRACTION

class MongoRepository:

    def __init__(self, connection_string, database_name):
        logger.info('Initialize. Database: {0}, HM_PRICE_DATA_RAW_EXTRACTION: "{1}".'.format(
            database_name, HM_PRICE_DATA_RAW_EXTRACTION))

        # http://api.mongodb.com/python/current/tutorial.html?_ga=1.114535310.822912736.1490913716

        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
