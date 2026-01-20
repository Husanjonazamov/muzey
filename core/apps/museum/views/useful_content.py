from rest_framework import viewsets
from core.apps.museum.models import UsefulContent
from core.apps.museum.serializers import UsefulContentSerializer

class UsefulContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UsefulContent.objects.all()
    serializer_class = UsefulContentSerializer
