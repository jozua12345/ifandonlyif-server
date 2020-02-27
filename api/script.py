import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
import json
from deals.models import Deals


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

with open('./onepair_crawler/onepair_crawler/spiders/data.json') as f:
    data = json.load(f)

for item in data:
    try:
        name = item['name']
    except KeyError:
        name = ""
    try:
        start = item['start']
    except KeyError:
        start = ""
    try:
        end = item['end']
    except KeyError:
        end = ""
    try:
        image = item['image']
    except KeyError:
        image = ""
    try:
        vendor = item['vendor']
    except KeyError:
        vendor = ""
    try:
        terms = item['terms']
        terms = deEmojify(terms)
    except KeyError:
        terms = ""
    try:
        category = item['category']
    except KeyError:
        category = ""

    '''
    print("1. Name: " + name)
    print("2. Start: " + start)
    print("3. End: " + end)
    print("4. Image: " + image)
    print(terms.encode())
    print("6. Category: " + category)
    print("===================================")'''
    if(not Deals.objects.all().filter(name=name)):
        print("Adding")
        deal = Deals(name=name, start=start, end=end, image=image, vendors=vendor, terms=terms, category=category)
        deal.save()
    
print("Success")
