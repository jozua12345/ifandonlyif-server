from django.shortcuts import render
from rest_framework import viewsets
from .models import Deals
from .serializers import DealsSerializer
# Create your views here.
class DealsView(viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer
