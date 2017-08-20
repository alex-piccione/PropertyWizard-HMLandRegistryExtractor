from datetime import datetime, date
import uuid

from extractor.repositories import logger, COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.repositories.mongoRepositoryBase import MongoRepositoryBase
from extractor.entities.saleRawData import SaleRawData


class SaleRawDataMongoRepository(MongoRepositoryBase):

    def __init__(self, connection_string, database):
        super().__init__(connection_string, database, COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION)


    def save(self, item: SaleRawData) -> int:

        _id = uuid.uuid4()  # random
        create_date = datetime.utcnow()

        self._change_date_to_datetime(item)  # apparently MongoDB cannot store datetime without the time part

        document = {
            "_id": _id,
            "create_date": create_date,

            "transaction_id": item.transaction_id,
            "price": item.price,
            "date": item.date,
            "post_code": item.post_code,
            "property_type": item.property_type,
            "new_build": item.new_build,
            "holding_type": item.holding_type,

            "paon": item.paon,
            "saon": item.saon,
            "street": item.street,
            "locality": item.locality,
            "city": item.city,
            "district": item.district,
            "county": item.county,

            "transaction_category": item.transaction_category,
            "action": item.action
        }

        result = self.collection.insert_one(document)

        if result.acknowledged:
            return result.inserted_id
        else:
            logger.fatal(f'{self.__class__} .save(...) return "Not acknowledged". Transaction Id: "{item.transaction_id}".')
            raise Exception("Not acknowledged")


    def list(self, start_date: datetime):

        filter_ = {"date": {"$gte": start_date}}
        result = self.collection.find(filter_)
        items = []
        for document in result:
            item = self._parse_document(document)
            items.append(item)
        return items


    def list_by_id(self, ids: list):

        filter_ = {"_id": {"$in": ids}}
        result = self.collection.find(filter_)
        items = []
        for document in result:
            item = self._parse_document(document)
            items.append(item)
        return items


    def _parse_document(self, document) -> SaleRawData:

        try:
            _id = document["_id"]
            create_date = document["create_date"]

            transaction_id = document["transaction_id"]
            price = document["price"]
            date_ = document["date"]
            post_code = document["post_code"]
            property_type = document["property_type"]
            new_build = document["new_build"]
            holding_type = document["holding_type"]
            paon = document["paon"]
            saon = document["saon"]
            street = document["street"]
            locality = document["locality"]
            city = document["city"]
            district = document["district"]
            county = document["county"]
            transaction_category = document["transaction_category"]
            action = document["action"]

            data = SaleRawData(transaction_id, price, date_, post_code,
                               property_type, new_build, holding_type,
                               paon, saon, street, locality, city, district, county,
                               transaction_category, action)

            data.id = _id
            data.create_date = create_date

            return data

        except Exception as error:
            logger.fatal(f"Fail to parse database document. Document: {document}. Error: {error}")
            raise ValueError(f"Fail to parse database document. Document: {document}.", error)


    def _change_date_to_datetime(self, item):

        if type(item.date) is date:
            item.date = datetime.combine(item.date, datetime.min.time())
