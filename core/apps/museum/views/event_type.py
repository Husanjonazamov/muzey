# views.py
from rest_framework import viewsets
from core.apps.museum.models import EventType
from core.apps.museum.serializers import EventTypeSerializer


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
