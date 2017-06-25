from pymongo import MongoClient
from datetime import datetime

from extractor.repositories import logger, \
    COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.entities.rawSellData import RawSellData

class SellDataMongoRepository:

    def __init__(self, connection_string, database_name):
        logger.info('Initialize. Database: {0}, HM_PRICE_DATA_RAW_EXTRACTION: "{1}".'.format(
            database_name, COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION))

        # http://api.mongodb.com/python/current/tutorial.html?_ga=1.114535310.822912736.1490913716

        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]

    def save(self, item: RawSellData) -> int:

        import random
        import sys

        _id = random.randint(1, sys.maxsize)

        document = {
            "_id": _id,
            "create_date": datetime.utcnow(),

            "transaction_id": item.transaction_id,
            "price": item.price,
            "date": item.date,
            "post_code": item.post_code,
            "property_type": item.property_type,
            "yn": item.yn,
            "holding_type": item.holding_type,

            "paon": item.paon,
            "saon": item.saon,
            "street": item.street,
            "locality": item.locality,
            "city": item.city,
            "district": item.district,
            "county": item.county,

            "x": item.x,
            "action": item.action
        }

        result = self.db[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION].insert_one(document)

        if result.acknowledged:
            return result.inserted_id
        else:
            raise Exception("Not acknowledged")

    def list(self, start_date):
        filter_ = {"date": {"$gte": start_date}}
        result = self.db[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION].find(filter_)
        items = list(result)
        return items

