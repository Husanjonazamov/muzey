from rest_framework import viewsets
from core.apps.museum.models import WorkingTime
from core.apps.museum.serializers import WorkingTimeSerializer

class WorkingTimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
