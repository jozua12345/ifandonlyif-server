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
    path('getFoodDeals/', api.getFoodDeals),
    path('getEntertainmentDeals/', api.getEntertainmentDeals),
    path('getRetailDeals/', api.getRetailDeals),
    path('getOthersDeals/', api.getOthersDeals),
    path('addUser/<uid>', api.addUser),
    path('updateToken/<uid>/<token>', api.updateToken),
    path('addBlacklist/<dealid>/<uid1>/<uid2>', api.addBlacklist),
    #<c> is a string of ids of choices separated by commas
    #eg <1,2,3,4,5>
    path('addRequest/<uid>/<dealid>/<c>', api.addRequest),
    path('addRequest2/<uid>/<dealid>/<c>', api.addRequest2),
    path('deleteRequest/<uid>/<dealid>', api.deleteRequest),
    path('getRequestById/<uid>', api.getRequestById),
    path('getAllLocation', api.getAllLocation),
    path('matchTrigger2', api.matchTrigger2),
]
