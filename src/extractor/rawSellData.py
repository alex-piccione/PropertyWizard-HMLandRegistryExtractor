class RawSellData:

    def __init__(self, guid, price,date, postcode, propertyType, yn, holdType,
                 paon, saon, street, locality, city, district, county, x, action
                 ):

        self.guid = guid
        self.price = price
        self.date = date
        self.postcode = postcode
        self.type = propertyType
        self.yn = yn
        self.holdType = holdType

        self.paon = paon
        self.saon = saon
        self.street = street
        self.locality = locality
        self.city = city
        self.district = district
        self.county = county

        self.x = x
        self.action = action
