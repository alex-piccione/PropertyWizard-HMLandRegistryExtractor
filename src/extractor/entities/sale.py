from uuid import UUID
from datetime import datetime

class Sale():

    def __init__(self, raw_data_id: UUID, partial_post_code, post_code, city, address, property_type: str, date: datetime, price: float, new_build: bool):

        self.raw_data_id = raw_data_id
        self.partial_post_code = partial_post_code
        self.post_code = post_code
        self.city = city
        self.address = address
        self.property_type = property_type
        self.date = date
        self.price = price
        self.new_build = new_build  # indicates if it is a new building

    def __str__(self):

        return f"post_code: {self.post_code}, date: {self.date}, address: {self.address}";