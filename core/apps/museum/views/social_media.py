from rest_framework import viewsets
from core.apps.museum.models import SocialMedia
from core.apps.museum.serializers import SocialMediaSerializer

class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
