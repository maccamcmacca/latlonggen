#!/usr/bin/env python

#Requires: input.json - {"town": "Dundee", "lat1": "56.478310", "lon1": "-3.050414", "lat2": "56.468327", "lon2": "-2.928002" }
import random
import time
import geojson
import json
from geojson import LineString, Point, FeatureCollection, Feature


#Read Input json file
f=open("input.json", "r")
jstr = f.read()
print(jstr)
towns = json.loads(jstr)

#Dundee Coordinates
latitude1 = 56.478310
longitude1 = -3.050414
latitude2 = 56.468327
longitude2 = -2.928002

#Misc Vars
setLength = 30
maxIntensity = 100
maxYear = 1918
minYear = 1914
maxMonth = 12
minMonth = 1
maxDay = 28
minDay = 1

def generateISODate():
	y = random.randint(minYear, maxYear)
	m = random.randint(minMonth, maxMonth)
	d = random.randint(minDay, maxDay)

	m_str = ""
	d_str = ""

	if(m < 10):
		m_str = str("0" + str(m))
	else:
		m_str = str(m)

	if(d < 10):
		d_str = str("0" + str(d))
	else:
		d_str = str(d)


	return str(y) + '-' + m_str + '-' + d_str



feats = []
idvar = 0
for y in range(0, len(towns)):

	latitude1 = float(towns[y]["lat1"])
	longitude1 = float(towns[y]["lon1"])
	latitude2 = float(towns[y]["lat2"])
	longitude2 = float(towns[y]["lon2"])

	for x in range(0, setLength):

		#Generate Random Coordinates for features
		rand_lat1 = random.uniform(latitude1, latitude2)
		rand_lon1 = random.uniform(longitude1, longitude2)
		rand_lat2 = random.uniform(latitude1, latitude2)
		rand_lon2 = random.uniform(longitude1, longitude2)

		intensity = random.randint(0, maxIntensity)
		curdate = generateISODate()

		#Create LineString and Point features
		line=Feature(geometry=LineString([(rand_lon1, rand_lat1),(rand_lon2, rand_lat2)]), id=(idvar), properties={"date": curdate})
		point=Feature(geometry=Point((rand_lon2, rand_lat2)), id=(idvar+1), properties={"date": curdate, "intensity": intensity, "town": towns[y]["town"]})

		#increment ID value
		idvar = idvar + 2

		#Add new features to FeatureCollection
		feats.append(line)
		feats.append(point)

feat_col = FeatureCollection(feats)
print("GeoJSON validity: " + str(feat_col.is_valid) + '\n')

f = open("raw.json", "w")
f.write(geojson.dumps(feat_col))

f = open("formatted.json", "w")
f.write(geojson.dumps(feat_col, indent=4))
