from rest_framework import viewsets
from django.db.models import Q
from rest_framework.permissions import AllowAny
from core.apps.museum.models import Exhibit
from core.apps.museum.serializers import ExhibitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ExhibitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exhibit.objects.all().order_by('-created_at')
    serializer_class = ExhibitSerializer

    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', None)
        search = request.query_params.get('search', None)
        type_id = request.query_params.get('type', None)  # Add type filter

        exhibits = Exhibit.objects.all().order_by('-created_at')
        total_count = exhibits.count()

        if search:
            search_filter = (
                Q(name_uz__icontains=search) |
                Q(name_ru__icontains=search) |
                Q(name_en__icontains=search) |
                Q(name_uz_Cyrl__icontains=search)
            )
            exhibits = exhibits.filter(search_filter)
            total_count = exhibits.count()

        if type_id:
            try:
                type_id = int(type_id)
                exhibits = exhibits.filter(type_id=type_id)
                total_count = exhibits.count()

            except ValueError:
                return Response({'error': 'Type ID must be an integer'}, status=400)

        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return Response({'error': 'Invalid number specified'}, status=400)
            except ValueError:
                return Response({'error': 'Limit must be an integer'}, status=400)
            exhibits = exhibits[:limit]

        serializer = ExhibitSerializer(exhibits, many=True)

        return Response({
            'total_count': total_count,
            'count': len(exhibits),
            'results': serializer.data
        })
class RandomExhibitView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Exhibit.objects.all()
        total_count = queryset.count()

        if total_count <= 4:
            exhibits = queryset
        else:
            exhibits = queryset.order_by('?')[:4]

        serializer = ExhibitSerializer(exhibits, many=True)

        return Response({
            'total_count': total_count,
            'count': len(exhibits),
            'results': serializer.data
        }, status=status.HTTP_200_OK)



