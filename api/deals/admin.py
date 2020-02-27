from django.contrib import admin
from .models import Deals, ClientUsers, BlackLists

# Register your models here.
admin.site.register(Deals)
admin.site.register(ClientUsers)
admin.site.register(BlackLists)