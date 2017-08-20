from uuid import UUID
from datetime import datetime

class SaleRawData():

    def __init__(self, transaction_id: UUID, price: float, date: datetime, post_code: str, property_type: str, new_build: str, holding_type: str,
                 paon: str, saon: str, street: str, locality: str, city: str, district: str, county: str, transaction_category: str, action: str
                 ):

        self.id = None
        self.create_date = None

        self.transaction_id = transaction_id
        self.price = price
        self.date = date  # ensure it is a datetime before saving it on MongoDB to avoid error
        self.post_code = post_code
        self.property_type = property_type
        self.new_build = new_build
        self.holding_type = holding_type

        self.paon = paon
        self.saon = saon
        self.street = street
        self.locality = locality
        self.city = city
        self.district = district
        self.county = county

        self.transaction_category = transaction_category
        self.action = action
