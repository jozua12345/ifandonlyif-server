from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('deals', views.DealsView)
router.register('clientusers', views.ClientUsersView)
router.register('blacklists', views.BlackListsView)
urlpatterns = [
    path('', include(router.urls)),
]
