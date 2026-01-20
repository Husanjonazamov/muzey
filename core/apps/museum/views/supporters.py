from rest_framework import generics

from core.apps.museum.models import Supporters
from core.apps.museum.serializers import SupportersSerializer

class SupportersListView(generics.ListAPIView):
    queryset = Supporters.objects.all()
    serializer_class = SupportersSerializer

class SupportersDetailView(generics.RetrieveAPIView):
    queryset = Supporters.objects.all()
    serializer_class = SupportersSerializer
