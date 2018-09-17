#!/usr/bin/env python

import random
import time
from geojson import LineString, Point, FeatureCollection, Feature
import geojson

#Dundee Coordinates
latitude1 = 56.478310
longitude1 = -3.050414
latitude2 = 56.468327
longitude2 = -2.928002

#Misc Vars
setLength = 5 #51
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
for x in range(0, setLength):

	#Generate Random Coordinates for features
	rand_lat1 = random.uniform(latitude1, latitude2)
	rand_lon1 = random.uniform(longitude1, longitude2)
	rand_lat2 = random.uniform(latitude1, latitude2)
	rand_lon2 = random.uniform(longitude1, longitude2)

	intensity = random.randint(0, maxIntensity)
	curdate = generateISODate()
	y = x*2		#use to set ID for both features

	#Create LineString and Point features
	line=Feature(geometry=LineString([(rand_lat1,rand_lon1),(rand_lat2,rand_lon2)]), id=(y), properties={"date": curdate})
	point=Feature(geometry=Point((rand_lat2, rand_lon2)), id=(y+1), properties={"date": curdate, "intensity": intensity})

	#Add new features to FeatureCollection
	feats.append(line)
	feats.append(point)

feat_col = FeatureCollection(feats)
print("GeoJSON validity: " + str(feat_col.is_valid) + '\n')

f = open("raw.json", "w")
f.write(geojson.dumps(feat_col))

f = open("formatted.json", "w")
f.write(geojson.dumps(feat_col, indent=4))
