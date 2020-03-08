import json
import requests
from django.http import HttpResponse
from .models import Deals, ClientUsers, BlackLists, Choices, Requests
from .serializers import DealsSerializer, BlackListsSerializer, ClientUsersSerializer, ChoicesSerializer, RequestsSerializer


FCM_ENDPOINT = 'https://fcm.googleapis.com/fcm/send'
FCM_KEY = 'AAAAzfk1l5E:APA91bFnzxOs2ne4MKnQM4qAKqBNE6UjiQqOA3og3Ud4xBlZU0KL9OJUDuzFdf6Suvy7lqd-hlxsYGPXUJjCS7qSHstixiCes1mDhpLY8-ZsykRkHQwVYtUaktGagNrd1AUvRFIq9usF'
FCM_USER = '884649334673'
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

def updateToken(request, uid, token):
    clientuser = ClientUsers.objects.get(uid=uid)
    clientuser.token = token

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
        matchTrigger()
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


def matchTrigger():
    queryset = Requests.objects.all()
    queueidRecent = queryset[len(queryset)-1]['id']
    uidRecent = queryset[len(queryset)-1]['clientuser']
    dealRecent = queryset[len(queryset)-1]['deal']
    choicesRecent = queryset[len(queryset)-1]['choices']
        
    for i in range(0,len(queryset)-1):
        if(queryset[i]['deal'] == dealRecent):
            if(set(choicesRecent) & set(queryset[i]['choices'])):
                clientuser1 = ClientUsers.objects.get(uid=uidRecent)
                clientuser2 = ClientUsers.objects.get(uid=queryset[i]['clientuser'])
                deal = Deals.objects.get(dealid=dealRecent)
                if(not(BlackLists.objects.get(clientuser1=clientuser1, clientuser2=clientuser2, deal=deal) 
                or BlackLists.objects.get(clientuser1=clientuser2, clientuser2=clientuser1, deal=deal))):
                    data1 = {}
                    body1 = []
                    body1.append(json.dumps(ClientUsersSerializer(clientuser1, many=False)))
                    body1.append(json.dumps(ClientUsersSerializer(clientuser2, many=False)))
                    body1.append(json.dumps(DealsSerializer(deal, many=False)))
                    data1['notification'] = {}
                    data1['notification']['title'] = "Found a match!"
                    data1['notification']['body'] = body1
                    data1['notification']['icon'] = "firebase-logo.png"
                    data1['notification']['click_action'] = "http://localhost:8081"
                    data1['to'] = clientuser1.token

                    data2 = {}
                    body2 = []
                    body2.append(json.dumps(ClientUsersSerializer(clientuser1, many=False)))
                    body2.append(json.dumps(ClientUsersSerializer(clientuser2, many=False)))
                    body2.append(json.dumps(DealsSerializer(deal, many=False)))
                    data2['notification'] = {}
                    data2['notification']['title'] = "Found a match!"
                    data2['notification']['body'] = body2
                    data2['notification']['icon'] = "firebase-logo.png"
                    data2['notification']['click_action'] = "http://localhost:8081"
                    data2['to'] = clientuser2.token

                    requests.post(FCM_ENDPOINT, data = data1, auth=(FCM_USER, FCM_KEY))
                    requests.post(FCM_ENDPOINT, data = data2, auth=(FCM_USER, FCM_KEY))
                    break

                    '''
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