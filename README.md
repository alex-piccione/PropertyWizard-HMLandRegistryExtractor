# HM Land Registry Extractor
__part of: Property Wizard__  
__last update: 16 August 2017__

This program is an extractor of the HM Land Registry public data.  
The extracted data are stored for a successive use by the Property Wizard API.  
It is a Python script that run on scheduled times.


# How it works

The program can elaborate Price Paid Data CSV file obtained from HM Land Property.   
Thew process start with a call to main.py passing the CSV file to read.  
The CSV file is parsed and raw data is stored in the database.  
A second step is the extrapolation of custom data from the raw data and a new saving in the database.
The new data contains relevant data. The Address is composed using raw data fields.  
A partial post code is extracted (district) to be used a search key.  

Data contains a property ("action") which is still not clear how should be used.    
It indicates that the record can be a deletion or a change of previous one.  
It is also not clear what is the unique identifier of records (if exists).   

# HM Land Registry

The source of data is the "Price Paid data" taken from here: https://www.gov.uk/government/collections/price-paid-data

Single file: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads#single-file
CSV: http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv

Current month CSV: http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update-new-version.csv

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

### Example data

First record in 2017/05 CSV data file:

<pre>
Id:                     {4E95D757-1CA7-EDA1-E050-A8C0630539E2}
Price:                  970000	
Date:                   2002-05-31 00:00	
Post code:              SW3 2BZ	
Type:                   F	
New build:              N	
Holding type:           L	
PAON:                   46	
SAON:                   FLAT 4	
Street:                 EGERTON GARDENS
Locality:        
City:                   LONDON	
District:               KENSINGTON AND CHELSEA	
County:                 GREATER LONDON	
Transaction category    A	
Action:                 A
</pre>

# Description of the fields:
<pre>
- Id:                   It is a GUID wrapped in curly brackets. It is duplicated also for completely different properties. What is it related to?
- Price:                Sell price in GBP
- Date:                 The date of the sale
   - Year
   - Month
- Post code:            can be empty. 
   - Partial post code. Obtained form the 4 initial characters and removing the space return the partial post code.
- Type:                 D/F/O/S/T  (Detached, Semi-detached, Terraced, Flat, Other)
- new build:            Y/N, Is a new building?  
- Holding type:         L/F (Leasehold/Freehold)
- PAON:                 Primary addressable object name. Typically the house number or name
- SAON:                 Secondary Addressable Object Name. If there is a sub-building, for example the building is divided into flats, there will be a SAON.
- Street:
- Locality:
- City:                 Town or City
- District:
- County:
- Transaction category: A/B (A=Standard, B=Additional)
- action:               A/C/D (record status notation Add/Change/Delete)
</pre>
 
## Note
Some prices seems wrong. For example 1£ or 125 million of pounds.  
The second case could be an error inserting the value with a wrong decimal character resulting 100 times more, so it could be 1million, and it is possible compared to other apartment in the same building.


# Heroku

[Virtualenv and requirements.txt](https://devcenter.heroku.com/articles/getting-started-with-python#declare-app-dependencies)