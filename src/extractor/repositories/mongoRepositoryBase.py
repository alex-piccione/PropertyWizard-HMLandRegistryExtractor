from pymongo import MongoClient
from bson import CodecOptions, binary

from extractor.repositories import logger

class MongoRepositoryBase:

    def __init__(self, connection_string, database:str, collection:str):
        logger.info(f'Initialize. Database: "{database}. Colelction: {collection}"')

        # http://api.mongodb.com/python/current/tutorial.html?_ga=1.114535310.822912736.1490913716

        self.client = MongoClient(connection_string)
        self.db = self.client[database]

        codec_options = CodecOptions(uuid_representation = binary.STANDARD)
        self.collection = self.db.get_collection(collection, codec_options)