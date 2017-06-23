import unittest

from src.extractor.repository.mongoRepository import MongoRepository

class MongoRepositoryTest(unittest.TestCase):

    def test_init__should__create_client_and_db (self):

        connection_string = "connection_string"
        database_name = "database_name"

        repository = MongoRepository(connection_string, database_name)

        assert repository  # is not None
        assert repository.client
        assert repository.db




