from rest_framework import viewsets

from core.apps.museum.models import Symbol
from core.apps.museum.serializers import SymbolSerializer

class SymbolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
