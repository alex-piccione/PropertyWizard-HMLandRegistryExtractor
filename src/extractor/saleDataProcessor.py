from datetime import datetime
import math
from typing import List
from extractor.entities.saleRawData import SaleRawData
from extractor.entities.sale import Sale
from extractor.repositories.saleMongoRepository import SaleMongoRepository
from extractor.repositories.saleRawDataMongoRepository import SaleRawDataMongoRepository
from extractor.exceptions.processSaleError import ProcessSaleError


class SaleDataProcessor():


    def __init__(self, sale_raw_data_repository: SaleRawDataMongoRepository, sale_repository: SaleMongoRepository):
        self.sale_raw_data_repository = sale_raw_data_repository
        self.sale_repository = sale_repository
        self.errors = None


    def process_new_records(self, record_ids: list):
        """
        Read the raw sale from the repository and process them.
        Creates rich sale data and save them in the repository.
        """

        self.errors = []

        try:
            raw_sales = self.sale_raw_data_repository.list_by_id(record_ids)
        except Exception as error:
            raise Exception("Fail to load raw sales", error)

        try:
            self._process_sales(raw_sales)
        except Exception as error:
            raise Exception("Fail to process raw sales", error)


    def _process_sales(self, raw_sales: List[SaleRawData]):

        for raw_sale in raw_sales:
            try:
                partial_post_code = self._get_partial_post_code(raw_sale.post_code)
                address = self._get_complete_address(raw_sale)

                sale = Sale(partial_post_code, post_code=raw_sale.post_code,
                            city=raw_sale.city, address=address,
                            property_type=raw_sale.property_type,
                            date=raw_sale.date, price=raw_sale.price, new_build=raw_sale.new_build)

                self.sale_repository.insert(sale)

            except Exception as error:
                self.errors.append(ProcessSaleError(raw_sale.id, error))


    def _get_partial_post_code(self, post_code: str):

        return post_code.split()[0] if post_code and " " in post_code else post_code


    def _get_complete_address(self, raw_data: SaleRawData):

        paon = f"{raw_data.paon}, " if raw_data.paon else ""
        address = f"{paon}{raw_data.saon} {raw_data.street} {raw_data.locality}".strip()
        return address
