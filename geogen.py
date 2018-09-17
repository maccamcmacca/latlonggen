import random
import time
from geojson import LineString

latitude1 = input("Enter latitude: ")
longitude1 = input("Enter longitude:")
latitude2 = input("Enter latitude: ")
longitude2 = input("Enter longitude:")

random.seed(time.clock)
print("Latitude")
for x in range(0,51):
	print(random.uniform(latitude1, latitude2))
print("longitude")
for x in range(0,51):
	print(random.uniform(longitude1, longitude2))
