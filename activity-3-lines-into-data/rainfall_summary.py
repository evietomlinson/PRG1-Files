"""
Rainfall Summary

Reads a month's rainfall from five weather stations and prints a
summary. Reading only: nothing is written back out.

Each line of rainfall.txt is a station name and a number of
millimetres, separated by a comma.
"""

WET_THRESHOLD = 100


with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0
wet_stations = []
dry_stations = []
driest_station = ""
lowest_rainfall = None
wettest_station = ""
highest_rainfall = None

for line in lines:
    station, millimetres_text = line.strip().split(",")
    millimetres = int(millimetres_text)

    total = total + millimetres
    count = count + 1

    if millimetres >= WET_THRESHOLD:
        wet_stations.append(station)
    else: 
         dry_stations.append(station)

    if lowest_rainfall is None or millimetres < lowest_rainfall:
       lowest_rainfall = millimetres
       driest_station = station

    if highest_rainfall is None or millimetres > lowest_rainfall:
              highest_rainfall = millimetres
              wettest_station = station
       

print(f"{count} stations reported") #2
print(f"Total rainfall: {total} mm") #479
print(f"Average: {total / count:.1f} mm") #95.8
print(f"At or above {WET_THRESHOLD} mm: {wet_stations}")
print(f"Driest station: {driest_station}")
print(f"Wettest station: {wettest_station}")
print(f"Stations below threshold: {len(dry_stations)}")