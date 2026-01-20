from rest_framework import serializers
from core.apps.museum.models import Gallery, Image

class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'image']

    def get_image(self, obj):
        return [image.image.url for image in obj.image.all()]