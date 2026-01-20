from rest_framework import viewsets

from core.apps.museum.models import ExhibitType
from core.apps.museum.serializers import ExhibitTypeSerializer


class ExhibitTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExhibitType.objects.all()
    serializer_class = ExhibitTypeSerializer
