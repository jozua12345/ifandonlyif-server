import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
import json
from deals.models import Requests, ClientUsers
from datetime import date


queryset = Requests.objects.all()
queryset.delete()
queryset2 = ClientUsers.objects.all()
queryset2.delete()
