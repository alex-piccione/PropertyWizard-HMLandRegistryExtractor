# Property Wizard - HM Land Registry Extractor
Data extractor of the HM Land Registry public data

# Source

https://www.gov.uk/government/collections/price-paid-data


# HM Land Registry

## 
When using or publishing our Price Paid Data
If you use or publish our price paid data, you must add the following attribution statement:

Data produced by HM Land Registry © Crown copyright 2017.
Price Paid Data is released under Open Government Licence (OGL). Under the OGL, HM Land Registry permits you to use the Price Paid Data for commercial or non-commercial purposes. However, OGL does not cover the use of third party rights, which we are not authorised to license.

Price Paid Data contains address data processed against Ordnance Survey’s AddressBase Premium product, which incorporates Royal Mail’s PAF® database (Address Data). Royal Mail and Ordnance Survey, permits your use of Address Data in the Price Paid Data:

for personal and/or non-commercial use
to display for the purpose of providing residential property price information services
If you want to use the Address Data in any other way, you must contact Royal Mail. Email address.management@royalmail.com.

## Address data

The following fields comprise the address data included in Price Paid Data:

- Postcode
- PAON Primary Addressable Object Name. Typically the house number or name.
- SAON Secondary Addressable Object Name. If there is a sub-building, for example the building is divided into flats, there will be a SAON.
- Street
- Locality
- Town/City
- District
- County

## Real data

First record in 2017/05 CSV data

Id:         {4E95D757-1CA7-EDA1-E050-A8C0630539E2}
Price:      970000	
Date:       2002-05-31 00:00	
Post code:  SW3 2BZ	
Type:       F	
??2:        N	
??3:        L	
PAON:       46	
SAON:       FLAT 4	
Street:     EGERTON GARDENS
Locality:        
City:       LONDON	
Ditrict:    KENSINGTON AND CHELSEA	
County:     GREATER LONDON	
??7:        A	
??8:        A

- Id:       it is a GUID wrapped in curly brackets
- Price:    Sell price in GBP
- Date:     Date of the sell?
   - Year
   - Month
- Post code: can be empty. 
   - Partial post code. Obtained form the 4 initial characters and removing the space return the partial post code.
- Type: Can be D/F/O/S/T  (Detached, Semi-detached, Terraced, Flat, Other)
- ??2: Can be Y/N, (Yes/No) (Leasehold) 
- Lasehold/Freehold: Can be: L/F (Leasehold, Freehold)
- PAON: Primary addressable object name. Typically the house number or name
- SAON: Secondary Addressable Object Name. If there is a sub-building, for example the building is divided into flats, there will be a SAON.
- Street:
- Locality:
- City:             Town or City
- District:
- County:
- ??7: can be A/B
- ??8: can be A/C/D  (record status notation? Add, Change, Delete ?)

  
Some prices seems wrong. For example 1£ or 125 million of pounds.  
The second case could be an error inserting the value with a wrong decimal character resulting 100 times more, so it could be 1million, and it is possible compared to other apartment in the same building.

# Heroku

[Virtualenv and requirements.txt](https://devcenter.heroku.com/articles/getting-started-with-python#declare-app-dependencies)