import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
import json
from deals.models import Choices

def readMRTStations():
    MRTStations = []
    with open('train-station-chinese-names.csv', newline='', encoding = 'utf8') as File:  
        reader = csv.reader(File)
        #extract english names of train station
        for row in reader:
            MRTStations.append(row[1])
        #remove header
        MRTStations.pop(0)
        #remove duplicates in list
        MRTStations = list(dict.fromkeys(MRTStations))
        #sort stations by alphabetical order
        MRTStations.sort(key=str.lower)
    return MRTStations

mrt = readMRTStations()
for loc in mrt:
    choice = Choices(name=loc)
    choice.save()
print("Success!")
