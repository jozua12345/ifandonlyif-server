import json
from django.http import HttpResponse
from .models import Deals, ClientUsers, BlackLists, Choices, Requests
from .serializers import DealsSerializer, BlackListsSerializer, ClientUsersSerializer, ChoicesSerializer, RequestsSerializer

def getAllDeals(request):
    queryset = Deals.objects.all()
    serializer = DealsSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))

def getAllLocation(request):
    queryset = Choices.objects.all()
    serializer =ChoicesSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))

def getFoodDeals(request):
    queryset = Deals.objects.filter(category__contains='Food')
    serializer = DealsSerializer(queryset, many=True)
    print(serializer)
    return HttpResponse(json.dumps(serializer.data))

def getEntertainmentDeals(request):
    queryset = Deals.objects.filter(category__contains='Entertainment')
    serializer = DealsSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))

def getRetailDeals(request):
    queryset = Deals.objects.filter(category__contains='Retail')
    serializer = DealsSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))

def getOthersDeals(request):
    queryset = Deals.objects.filter(category__contains='Others')
    serializer = DealsSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))

def addUser(request, uid):
    clientuser = ClientUsers(uid=uid)
    try:
        clientuser.save()
        return HttpResponse('<H1>SUCCESS</H1>')
    except Exception as e:
        return HttpResponse('<H1>%s</H1>' %str(e))


def addBlacklist(request, dealid, uid1, uid2):
    clientuser1 = ClientUsers.objects.get(uid=uid1)
    clientuser2 = ClientUsers.objects.get(uid=uid2)
    pid = int(dealid)
    deal = Deals.objects.get(pk=pid)
    blacklist = BlackLists(clientuser2=clientuser2, clientuser1=clientuser1, deal=deal)

    try:
        blacklist.save()
        return HttpResponse('<H1>SUCCESS</H1>')
    except Exception as e:
        return HttpResponse('<H1>%s</H1>' %str(e))

def addRequest(request, uid, dealid, c):
    clientuser = ClientUsers.objects.get(uid=uid)
    deal = Deals.objects.get(pk=int(dealid))
    request = Requests(clientuser=clientuser, deal=deal)

    try:
        request.save()
        l = c.split(',')
        for i in l:
            choice = Choices.objects.get(pk=int(i))
            request.choices.add(choice)
        return HttpResponse('<H1>SUCCESS</H1>')
    except Exception as e:
        return HttpResponse('<H1>%s</H1>' %str(e))

def deleteRequest(request, uid, dealid):
    clientuser = ClientUsers.objects.get(uid=uid)
    deal = Deals.objects.get(pk=int(dealid))
    request = Requests.objects.get(clientuser=clientuser, deal=deal)
    try:
        request.delete()
        return HttpResponse('<H1>SUCCESS</H1>')
    except Exception as e:
        return HttpResponse('<H1>%s</H1>' %str(e))

def getRequestById(request, uid):
    clientuser = ClientUsers.objects.get(uid=uid)
    queryset = Requests.objects.filter(clientuser=clientuser)
    serializer = RequestsSerializer(queryset, many=True)
    return HttpResponse(json.dumps(serializer.data))
'''
def matchTrigger(request):
    queryset = Request.objects.all()
    queueidRecent = queryset[len(queryset)-1]['id']
    uidRecent = queryset[len(queryset)-1]['clientuser']
    dealRecent = queryset[len(queryset)-1]['deal']
    choicesRecent = queryset[len(queryset)-1]['choices']
        
    for i in range(0,len(queryset)-1):
        if(queryset[i]['deal'] == dealRecent):
            if(set(choicesRecent) & set(queryset[i]['choices'])):
                matchDict = {}
                matchDict['uid1'] = uidRecent
                matchDict['uid2'] = queryset[i]['clientuser']
                matchDict['deal'] = dealRecent
                matchDict['locations'] = list(set(choicesRecent) & set(queryset[i]['choices']))
                #remove both users from database
                SomeModel.objects.filter(id=queueidRecent).delete()
                SomeModel.objects.filter(id=queryset[i]['id']).delete()
                #send push-notification to both users
                return matchDict
'''