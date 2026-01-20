from django.conf import settings
from rest_framework import serializers
from core.apps.museum.models import Supporters

class SupportersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supporters
        fields = ('id', 'logo')