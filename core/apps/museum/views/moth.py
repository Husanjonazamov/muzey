from django.db.models import Q
from rest_framework import viewsets
from core.apps.museum.models import Moth, MothType
from core.apps.museum.serializers import MothSerializer, MothTypeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

class MothTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MothType.objects.all()
    serializer_class = MothTypeSerializer




class MothViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Moth.objects.all().order_by('-created_at')
    serializer_class = MothSerializer

    def list(self, request, *args, **kwargs):
        limit = request.query_params.get('limit', None)
        search = request.query_params.get('search', None)
        type_id = request.query_params.get('type', None)  # Add type filter

        moth_queryset = Moth.objects.all().order_by('-created_at')
        total_count = moth_queryset.count()

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
            moth_queryset = moth_queryset.filter(search_filter)
            total_count = moth_queryset.count()

        # Apply type filter
        if type_id:
            try:
                type_id = int(type_id)
                moth_queryset = moth_queryset.filter(type_id=type_id)
                total_count = moth_queryset.count()
            except ValueError:
                return Response({'error': 'Type ID must be an integer'}, status=400)

        # Apply limit
        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return Response({'error': 'Invalid number specified'}, status=400)
            except ValueError:
                return Response({'error': 'Limit must be an integer'}, status=400)
            moth_queryset = moth_queryset[:limit]

        # Serialize the queryset
        serializer = self.get_serializer(moth_queryset, many=True)

        # Return the response with total count, count of returned items, and results
        return Response({
            'total_count': total_count,
            'count': len(moth_queryset),
            'results': serializer.data
        })
