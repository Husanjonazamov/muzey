from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from core.apps.museum.models.about import About, Location, Address
from core.apps.museum.serializers import AboutSerializer, LocationSerializer, AddressSerializer


@method_decorator(never_cache, name='dispatch')
class AboutReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all().order_by('-id')[:1]
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]


@method_decorator(never_cache, name='dispatch')
class AddressReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.order_by('-id')[:1]
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]


@method_decorator(never_cache, name='dispatch')
class LocationReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.order_by('-id')[:1]
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]
