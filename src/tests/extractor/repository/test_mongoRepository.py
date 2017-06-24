import unittest
from datetime import date
from datetime import datetime
import uuid
from uuid import UUID
from pymongo import MongoClient


from src.extractor.repositories.mongoRepository import MongoRepository
from src.extractor.repositories import COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.entities.rawSellData import RawSellData

from tests.extractor import config  ## dev config

class MongoRepositoryTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        connection_string = config.mongo_connection_string
        database_name = config.mongo_database_name
        self.repository = MongoRepository(connection_string, database_name)
        self.database = MongoClient(connection_string)[database_name]

    def tearDown(self):
        pass


    def test_init__should__create_client_and_db (self):

        connection_string = "connection_string"
        database_name = "database_name"

        repository = MongoRepository(connection_string, database_name)

        assert repository  # is not None
        assert repository.client
        assert repository.db


    def test_save__should__populate_the_right_fields(self):

        transaction_id = uuid.uuid4()  # random
        price = 1.23
        date_ = datetime.today()
        post_code = "post code"
        property_type = "property_type"
        yn = "y"
        holding_type = "holding_type"
        paon = "paon"
        saon = "saon"
        street = "street"
        locality = "locality"
        city = "city"
        district = "district"
        county = "county"
        x = "x"
        action = "action"

        document = RawSellData(transaction_id, price, date_, post_code, property_type, yn, holding_type,
                               paon, saon, street, locality, city, district, county, x, action)

        try:
            # execute
            self.repository.save(document)

            saved_document: RawSellData = self._get_record(transaction_id)

            assert saved_document

            assert "transaction_id" in saved_document
            assert "date" in saved_document
            #self.assertEqual(saved_document.transaction_id, transaction_id, "transaction_id")
            #self.assertEqual(saved_document.date, date, "date")

        finally:
            self._delete_record(transaction_id)  # clean up


    # private utility

    def _get_record(self, transaction_id):

        document = self._get_collection().find_one({"transaction_id": transaction_id})
        return document

    def _delete_record(self, transaction_id):
        self._get_collection().delete_one({"transaction_id": transaction_id})

    def _get_collection(self):
        return self.database[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION]





