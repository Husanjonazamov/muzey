from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from core.apps.museum.models import VideoGallery
from core.apps.museum.serializers import VideoGallerySerializer

class VideoGalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer

    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', None)
        search = request.query_params.get('search', None)

        # Initialize the queryset
        queryset = VideoGallery.objects.all()
        total_count = queryset.count()

        # Apply search filter
        if search:
            search_filter = (
                Q(title_uz__icontains=search) |
                Q(title_ru__icontains=search) |
                Q(title_en__icontains=search) |
                Q(title_uz_Cyrl__icontains=search) |
                Q(text_uz__icontains=search) |
                Q(text_ru__icontains=search) |
                Q(text_en__icontains=search) |
                Q(text_uz_Cyrl__icontains=search)
            )
            queryset = queryset.filter(search_filter)
            total_count = queryset.count()

        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return Response({'error': 'Invalid number specified'}, status=400)
            except ValueError:
                return Response({'error': 'Limit must be an integer'}, status=400)
            queryset = queryset[:limit]

        # Serialize the queryset
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'total_count': total_count,
            'count': len(queryset),
            'results': serializer.data
        })
