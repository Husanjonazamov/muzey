from rest_framework import serializers
from core.apps.museum.models import Connect

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ('id', 'user_name', 'phone', 'massage')
