from rest_framework import viewsets

from core.apps.museum.models import MuseumHistory
from core.apps.museum.serializers import MuseumHistorySerializer


class MuseumHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MuseumHistory.objects.all()
    serializer_class = MuseumHistorySerializer
