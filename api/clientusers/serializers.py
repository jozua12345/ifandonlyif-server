from rest_framework import serializers
from .models import ClientUsers

class ClientUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUsers
        fields = '__all__'