
from pymongo import MongoClient
from datetime import datetime, date
import uuid
from bson import CodecOptions, binary

from extractor.repositories import logger, \
    COLLECTION_HM_SALE
from extractor.entities.saleRawData import SaleRawData


class SaleMongoRepository:







