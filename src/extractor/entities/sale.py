from datetime import datetime

class Sale():

    def __init__(self, partial_post_code, post_code, city, address, property_type: str, date: datetime, price: float):

        self.partial_post_code = partial_post_code
        self.post_code = post_code
        self.city = city
        self.address = address
        self.property_type = property_type
        self.date = date
        self.price = price
