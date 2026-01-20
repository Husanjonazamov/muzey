from rest_framework import serializers

from core.apps.museum.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )

        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                return request.build_absolute_uri(obj.image.url)
            return None