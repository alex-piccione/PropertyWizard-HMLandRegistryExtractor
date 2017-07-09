from extractor.entities.saleRawData import SaleRawData
from extractor.entities.sale import Sale

class SaleDataProcessor():


    def __init__(self):
        pass

    def process(self, raw_sales: list): #-> list

        sales = []

        for raw_sale in raw_sales:

            partial_post_code = self._get_partial_post_code(raw_sale)
            address = self._get_complete_address(raw_sale)

            sale = Sale(partial_post_code, post_code=raw_sale.post_code,
                                 city=raw_sale.city, address=address,
                                 property_type=raw_sale.property_type,
                                 date=raw_sale.date, price=raw_sale.price)

            sales.push(sale)

        return sales


    def _get_partial_post_code(self, post_code):

        return post_code.split()[0] if post_code and " " in post_code else post_code


        return post_code


    def _get_complete_address(self, raw_data: SaleRawData):

        paon = f"{raw_data.paon}, " if raw_data.paon else ""
        address = f"{paon}{raw_data.saon} {raw_data.street} {raw_data.locality}".strip()
        return address
