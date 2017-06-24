from pymongo import MongoClient
from datetime import datetime

from extractor.repositories import logger, \
    COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION

class MongoRepository:

    def __init__(self, connection_string, database_name):
        logger.info('Initialize. Database: {0}, HM_PRICE_DATA_RAW_EXTRACTION: "{1}".'.format(
            database_name, COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION))

        # http://api.mongodb.com/python/current/tutorial.html?_ga=1.114535310.822912736.1490913716

        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]

    def save(self, price_data):

        document = {
            "insert_date": datetime.utcnow(),

            "transaction_id": price_data.transaction_id,
            "date": price_data.date,
            "action": price_data.action
        }

        self.db[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION].insert_one(document)