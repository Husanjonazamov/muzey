from rest_framework import serializers
from core.apps.museum.models import SocialMedia

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'url', 'icon']
