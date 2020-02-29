from django.http import HttpResponse
from .models import Deals, ClientUsers, BlackLists, Choices, Requests
from .serializers import DealsSerializer, BlackListsSerializer, ClientUsersSerializer, ChoicesSerializer, RequestsSerializer

def getAllDeals(request):
    queryset = Deals.objects.all()
    serializer = DealsSerializer(queryset, many=True)
    return HttpResponse(serializer.data)

def addUser(request, uid, username):
    clientuser = ClientUsers(uid=uid, name=username)
    try:
        clientuser.save()
        return HttpResponse('<H1>SUCCESS</H1>')
    except Exception as e:
        return HttpResponse('<H1>%s</H1>' %str(e))
        