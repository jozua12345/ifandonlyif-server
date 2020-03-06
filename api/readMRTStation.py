import os
import django
import pandas as pd
import io
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
import json
from deals.models import Choices

def readMRTStations():
    mrtStations = []
    url = 'https://data.gov.sg/dataset/c89bb614-b4ac-4669-8c65-a2e2ea5211a6/download'
    s = requests.get(url).content
    ds = pd.read_csv(io.StringIO(s.decode('utf-8','ignore')), sep = '\r')
    ds = ds.join(ds.pop('PK').str.split(',', expand=True))
    ds = ds.iloc[57:len(ds)-1]
    #take the column containing english names of mrt station
    mrtStations = ds[1]
    mrtStations = mrtStations.values.tolist()
    #remove duplicates in list
    mrtStations = list(dict.fromkeys(mrtStations))
    #sort stations by alphabetical order, regardless of upper or lower case
    mrtStations.sort(key=str.lower)
    return mrtStations


mrt = readMRTStations()
for loc in mrt:
    if(not Choices.objects.all().filter(name=loc)):
        choice = Choices(name=loc)
        choice.save()
print("Success!")
