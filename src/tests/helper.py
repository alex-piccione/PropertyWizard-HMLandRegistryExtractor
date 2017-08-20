import uuid
from datetime import date
from extractor.entities.saleRawData import SaleRawData


def create_SaleRawData() -> SaleRawData:
    transaction_id = uuid.uuid4()  # random
    price = 1.23
    date_ = date(2002, 5, 31)
    post_code = "post code"
    property_type = "property type"
    new_build = "Y"
    holding_type = "holding type"
    paon = "paon"
    saon = "saon"
    street = "street"
    locality = "locality"
    city = "city"
    district = "district"
    county = "county"
    transaction_category = "B"
    action = "action"
    item = SaleRawData(transaction_id, price, date_, post_code, property_type, new_build, holding_type,
                       paon, saon, street, locality, city, district, county, transaction_category, action)

    return item