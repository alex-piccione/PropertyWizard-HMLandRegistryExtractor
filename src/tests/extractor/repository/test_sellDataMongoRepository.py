import unittest
from datetime import date
from datetime import datetime
import uuid
from uuid import UUID
from pymongo import MongoClient


from src.extractor.repositories.sellDataMongoRepository import SellDataMongoRepository
from src.extractor.repositories import COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.entities.rawSellData import RawSellData

from tests.extractor import config  ## dev config

class SellDataMongoRepositoryTest(unittest.TestCase):

    def setUp(self):
        connection_string = config.mongo_connection_string
        database_name = config.mongo_database_name
        self.repository = SellDataMongoRepository(connection_string, database_name)
        self.database = MongoClient(connection_string)[database_name]


    def test_init__should__create_client_and_db(self):
        connection_string = "connection_string"
        database_name = "database_name"
        repository = SellDataMongoRepository(connection_string, database_name)
        assert repository  # is not None
        assert repository.client
        assert repository.db

    def test_save__should__populate_the_right_fields(self):

        sell_data = self._create_RawSellData()

        try:
            # execute
            self.repository.save(sell_data)

            saved_document: RawSellData = self._get_record(sell_data.transaction_id)

            assert saved_document

            assert "transaction_id" in saved_document
            assert "price" in saved_document
            assert "date" in saved_document
            assert "post_code" in saved_document
            assert "property_type" in saved_document
            assert "yn" in saved_document
            assert "holding_type" in saved_document
            assert "paon" in saved_document
            assert "saon" in saved_document
            assert "street" in saved_document
            assert "locality" in saved_document
            assert "city" in saved_document
            assert "district" in saved_document
            assert "county" in saved_document
            assert "x" in saved_document
            assert "action" in saved_document

            self.assertEqual(saved_document["transaction_id"], sell_data.transaction_id, "transaction_id")
            self.assertEqual(saved_document["price"], sell_data.price, "price")
            self.assertEqualDate(saved_document["date"], sell_data.date, "date")
            self.assertEqual(saved_document["post_code"], sell_data.post_code, "post_code")
            self.assertEqual(saved_document["property_type"], sell_data.property_type, "property_type")
            self.assertEqual(saved_document["yn"], sell_data.yn, "yn")
            self.assertEqual(saved_document["holding_type"], sell_data.holding_type, "holding_type")
            self.assertEqual(saved_document["paon"], sell_data.paon, "paon")
            self.assertEqual(saved_document["saon"], sell_data.saon, "saon")
            self.assertEqual(saved_document["street"], sell_data.street, "street")
            self.assertEqual(saved_document["locality"], sell_data.locality, "locality")
            self.assertEqual(saved_document["city"], sell_data.city, "city")
            self.assertEqual(saved_document["district"], sell_data.district, "district")
            self.assertEqual(saved_document["county"], sell_data.county, "county")
            self.assertEqual(saved_document["x"], sell_data.x, "x")
            self.assertEqual(saved_document["action"], sell_data.action, "action")

        finally:
            self._delete_record(sell_data.transaction_id)  # clean up

    def test_save__should__set_basic_fields(self):

        sell_data = self._create_RawSellData()

        try:
            # execute
            self.repository.save(sell_data)

            saved_document: RawSellData = self._get_record(sell_data.transaction_id)

            assert saved_document

            assert "id_" in saved_document
            assert "create_date" in saved_document

            # self.assertIs(saved_document["insert_date"], ) # todo: check type
            # todo: check it is less than 5 seconds ago

        finally:
            self._delete_record(sell_data.transaction_id)  # clean up


    # private utility

    def _get_record(self, transaction_id):
        document = self._get_collection().find_one({"transaction_id": transaction_id})
        return document

    def _delete_record(self, transaction_id):
        self._get_collection().delete_one({"transaction_id": transaction_id})

    def _get_collection(self):
        return self.database[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION]

    def _create_RawSellData(self) -> RawSellData:
        transaction_id = uuid.uuid4()  # random
        price = 1.23
        date_ = datetime.today()
        post_code = "post code"
        property_type = "property type"
        yn = "y"
        holding_type = "holding type"
        paon = "paon"
        saon = "saon"
        street = "street"
        locality = "locality"
        city = "city"
        district = "district"
        county = "county"
        x = "x"
        action = "action"
        item = RawSellData(transaction_id, price, date_, post_code, property_type, yn, holding_type,
                           paon, saon, street, locality, city, district, county, x, action)

        return item


    def assertEqualDate(self, first: datetime, second: datetime, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first.year, second.year, msg=msg)
        assertion_func(first.month, second.month, msg=msg)
        assertion_func(first.day, second.day, msg=msg)
        assertion_func(first.hour, second.hour, msg=msg)
        assertion_func(first.minute, second.minute, msg=msg)
        assertion_func(first.second, second.second, msg=msg)
