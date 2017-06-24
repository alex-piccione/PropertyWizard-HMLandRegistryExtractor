from uuid import UUID
from datetime import datetime

class RawSellData:

    def __init__(self, transaction_id: UUID, price: float, date: datetime, post_code: str, property_type: str, yn: str, holding_type: str,
                 paon: str, saon: str, street: str, locality: str, city: str, district: str, county: str, x: str, action: str
                 ):

        self.transaction_id = transaction_id
        self.price = price
        self.date = date
        self.post_code = post_code
        self.type = property_type
        self.yn = yn
        self.holding_Type = holding_type

        self.paon = paon
        self.saon = saon
        self.street = street
        self.locality = locality
        self.city = city
        self.district = district
        self.county = county

        self.x = x
        self.action = action
