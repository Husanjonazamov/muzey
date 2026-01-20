from rest_framework import viewsets
from core.apps.museum.models import Image
from core.apps.museum.serializers import ImageSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
