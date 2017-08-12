from datetime import datetime, date
import uuid

from extractor.repositories import logger, COLLECTION_HM_SALE
from extractor.repositories.mongoRepositoryBase import MongoRepositoryBase
from extractor.entities.sale import Sale


class SaleMongoRepository(MongoRepositoryBase):
    """
    Contains the rich information about a sale.
    It is created using raw data from HR Land Registry and some extrapolation like the Year and the partial post code.
    """


    def __init__(self, connection_string, database):
        super().__init__(connection_string, database, COLLECTION_HM_SALE)


    def insert(self, sale:Sale):

        _id = uuid.uuid4()  # random
        create_date = datetime.utcnow()

        document = {
            "_id": _id,
            "create_date": create_date,

            "transaction_id": sale.transaction_id,
            "price": sale.price,
            "date": sale.date,

            "post_code": sale.post_code,
            "partial_post_code": sale.partial_post_code,
            "city": sale.city,
            "address": sale.address,
            "property_type": sale.property_type
        }

        result = self.collection.insert_one(document)

        if result.acknowledged:
            return result.inserted_id
        else:
            logger.fatal(f'{self.__class__} .save(...) return "Not acknowledged". Transaction Id: "{item.transaction_id}".')
            raise Exception("Not acknowledged")

