from rest_framework import viewsets

from core.apps.museum.models import Management
from core.apps.museum.serializers import ManagementSerializer


class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
