from pymongo import MongoClient
from datetime import datetime, date
import uuid

from extractor.repositories import logger, \
    COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.entities.rawSellData import RawSellData


class SellDataMongoRepository:

    def __init__(self, connection_string, database_name):
        logger.info('Initialize. Database: "{0}", HM_PRICE_DATA_RAW_EXTRACTION: "{1}".'.format(
            database_name, COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION))

        # http://api.mongodb.com/python/current/tutorial.html?_ga=1.114535310.822912736.1490913716

        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]


    def save(self, item: RawSellData) -> int:

        _id = uuid.uuid4()  # random
        create_date = datetime.utcnow()

        self._change_date_to_datetime(item)

        document = {
            "_id": _id,
            "create_date": create_date,

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
        items = []
        for document in result:
            item = self._parse_document(document)
            items.append(item)
        return items


    def _parse_document(self, document) -> RawSellData:

        try:
            _id = document["_id"]
            create_date = document["create_date"]

            transaction_id = document["transaction_id"]
            price = document["price"]
            date_ = document["date"]
            post_code = document["post_code"]
            property_type = document["property_type"]
            yn = document["yn"]
            holding_type = document["holding_type"]
            paon = document["paon"]
            saon = document["saon"]
            street = document["street"]
            locality = document["locality"]
            city = document["city"]
            district = document["district"]
            county = document["county"]
            x = document["x"]
            action = document["action"]

            data = RawSellData(transaction_id, price, date_, post_code,
                               property_type, yn, holding_type,
                               paon, saon, street, locality, city, district, county,
                               x, action)

            data.id = _id
            data.create_date = create_date

            return data

        except Exception as error:
            raise ValueError(f"Fail to parse database document. Document: {document}.", error)


    def _change_date_to_datetime(self, item):

        if type(item.date) is date:
            item.date = datetime.combine(item.date, datetime.min.time())
