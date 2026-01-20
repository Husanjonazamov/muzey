from rest_framework import viewsets
from core.apps.museum.models import PriceSection, PriceText
from core.apps.museum.serializers import PriceSectionSerializer, PriceTextSerializer


class PriceSectionListView(viewsets.ReadOnlyModelViewSet):
    queryset = PriceSection.objects.all()
    serializer_class = PriceSectionSerializer

class PriceTextView(viewsets.ReadOnlyModelViewSet):
    queryset = PriceText.objects.all()
    serializer_class = PriceTextSerializer
