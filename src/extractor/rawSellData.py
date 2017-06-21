class RawSellData:

    def __init__(self, guid, price, date, post_code, property_type, yn, holding_Type,
                 paon, saon, street, locality, city, district, county, x, action
                 ):

        self.guid = guid
        self.price = price
        self.date = date
        self.post_code = post_code
        self.type = property_type
        self.yn = yn
        self.holding_Type = holding_Type

        self.paon = paon
        self.saon = saon
        self.street = street
        self.locality = locality
        self.city = city
        self.district = district
        self.county = county

        self.x = x
        self.action = action
