from rest_framework import serializers
from .models import Deals, ClientUsers, BlackLists

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = '__all__'

class ClientUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUsers
        fields = '__all__'

class BlackListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackLists
        fields = '__all__'