import unittest
from datetime import date, datetime, timedelta
import uuid
from pymongo import MongoClient

from src.extractor.repositories.sellDataMongoRepository import SellDataMongoRepository
from src.extractor.repositories import COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION
from extractor.entities.rawSellData import RawSellData

from tests.extractor import config  # dev config

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

            saved_document: RawSellData = self._get_document(sell_data.transaction_id)

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

            saved_document: RawSellData = self._get_document(sell_data.transaction_id)

            assert saved_document

            assert "_id" in saved_document
            assert "create_date" in saved_document

            # self.assertIs(saved_document["insert_date"], ) # todo: check type
            # todo: check it is not before 5 seconds ago

        finally:
            self._delete_record(sell_data.transaction_id)  # clean up


    def test_list(self):

        start_date = datetime.utcnow() - timedelta(days=1)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)

        old_item = self._create_RawSellData()
        old_item.date = start_date - timedelta(days=1)

        new_item = self._create_RawSellData()
        new_item.date = start_date

        try:
            old_id = self._save_item(old_item)
            new_id = self._save_item(new_item)

            # execute
            items = self.repository.list(start_date)

            assert items
            assert isinstance(items, list)

            assert len(items) > 0
            assert isinstance(items[0], RawSellData)

            assert len(list(filter(lambda i: i.id == old_id, items))) == 0
            assert len(list(filter(lambda i: i.id == new_id, items))) == 1

        finally:
            self._delete_document(old_id)
            self._delete_document(new_id)

    def test_parse_document(self):

        _id = None

        try:

            item = self._create_RawSellData()
            _id = self._save_item(item)
            document = self._get_document(item.transaction_id)

            # execute
            item = self.repository._parse_document(document)

            assert isinstance(item, RawSellData)

            self.assertEqual(item.transaction_id, document["transaction_id"])
            self.assertEqual(item.price, document["price"])
            document_date = document["date"]
            self.assertEqualDate(item.date, document_date)
            self.assertEqual(item.post_code, document["post_code"])
            self.assertEqual(item.property_type, document["property_type"])
            self.assertEqual(item.yn, document["yn"])
            self.assertEqual(item.holding_type, document["holding_type"])

            self.assertEqual(item.paon, document["paon"])
            self.assertEqual(item.saon, document["saon"])
            self.assertEqual(item.street, document["street"])
            self.assertEqual(item.locality, document["locality"])
            self.assertEqual(item.city, document["city"])
            self.assertEqual(item.district, document["district"])
            self.assertEqual(item.county, document["county"])

            self.assertEqual(item.x, document["x"])
            self.assertEqual(item.action, document["action"])

        finally:
            if _id:
                self._delete_document(_id)


    # private utility

    def _get_document(self, transaction_id) -> dict:
        document = self._get_collection().find_one({"transaction_id": transaction_id})
        return document

    def _delete_record(self, transaction_id):
        self._get_collection().delete_one({"transaction_id": transaction_id})

    def _delete_document(self, _id):
        self._get_collection().delete_one({"_id": _id})

    def _get_collection(self):
        return self.database[COLLECTION_HM_PRICE_DATA_RAW_EXTRACTION]

    def _save_item(self, sell_data):
        id = self.repository.save(sell_data)
        return id

    def _create_RawSellData(self) -> RawSellData:
        transaction_id = uuid.uuid4()  # random
        price = 1.23
        date_ = date(2002, 5, 31)
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
