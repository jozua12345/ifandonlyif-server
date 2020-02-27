from django.shortcuts import render
from rest_framework import viewsets
from .models import Deals, ClientUsers, BlackLists
from .serializers import DealsSerializer, BlackListsSerializer, ClientUsersSerializer
# Create your views here.
class DealsView(viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer

class ClientUsersView(viewsets.ModelViewSet):
    queryset = ClientUsers.objects.all()
    serializer_class = ClientUsersSerializer

class BlackListsView(viewsets.ModelViewSet):
    queryset = BlackLists.objects.all()
    serializer_class = BlackListsSerializer
