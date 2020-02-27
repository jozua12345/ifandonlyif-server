from django.shortcuts import render
from rest_framework import viewsets
from .models import ClientUsers
from .serializers import ClientUsersSerializer
# Create your views here.
class ClientUsersView(viewsets.ModelViewSet):
    queryset = ClientUsers.objects.all()
    serializer_class = ClientUsersSerializer
