import random
import time
import json

#print("Enter latitude: ")
latitude1 = input("Enter latitude: ")
longitude1 = input("Enter longitude:")
latitude2 = input("Enter latitude: ")
longitude2 = input("Enter longitude:")

random.seed(time.clock)
print("Latitude")
for x in range(0,51):
	lat = random.uniform(latitude1, latitude2)
	long = random.uniform(longitude1, longitude2)
	print long
	print lat
	x = {
		"Latitude":lat,
		"Longitude":long

	}
	x = json.dumps(x)
	with open('data.json', 'a') as outfile:
		json.dump(x, outfile)
	print '\n'

print(x)
#print("longitude")
#for x in range(0,51):
	