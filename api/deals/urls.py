from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register('deals', views.DealsView)
router.register('clientusers', views.ClientUsersView)
router.register('blacklists', views.BlackListsView)
router.register('choices', views.ChoicesView)
router.register('requests', views.RequestsView)
urlpatterns = [
    path('', include(router.urls)),
    path('getAllDeals/', api.getAllDeals),
    path('addUser/<uid>/<username>', api.addUser)
]
