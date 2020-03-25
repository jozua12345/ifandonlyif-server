import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
import json
from deals.models import Requests, ClientUsers
from datetime import date


clientuser = ClientUsers.objects.get(uid='ShxycWR07JRzaY6FZ6qKZXmeR8d2')
clientuser.delete()
