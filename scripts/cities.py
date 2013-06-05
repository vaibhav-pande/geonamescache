# -*- coding: utf-8 -*-
import csv
import json

cities = {}
fcsv = open('../data/cities15000.txt', 'r')
reader = csv.reader(fcsv, 'excel-tab')
headers = next(reader)
for record in reader:
    (geonameid, name, asciiname, alternatenames, latitude, longitude,
    featureclass, featurecode, countrycode, cc2, admin1code, admin2code,
    admin3code, admin4code, population, elevation, dem, timezone,
    modificationdate) = record

    # required because used as key
    if not geonameid:
        continue

    cities[geonameid] = {
        'geonameid': geonameid,
        'name': name,
        'latitude': latitude,
        'longitude': longitude,
        'countrycode': countrycode,
        'population': population,
        'timezone': timezone
    }

fcities = open('../geonamescache/cities.json', 'w')
json.dump(cities, fcities)
fcities.close()
