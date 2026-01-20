from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.db.models import Q

from core.apps.museum.models import Product
from core.apps.museum.serializers import ProductSerializer

class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            search_filter = (
                Q(name_uz__icontains=search) |
                Q(name_ru__icontains=search) |
                Q(name_en__icontains=search) |
                Q(name_uz_Cyrl__icontains=search) |
                Q(desc_uz__icontains=search) |
                Q(desc_ru__icontains=search) |
                Q(desc_en__icontains=search) |
                Q(desc_uz_Cyrl__icontains=search)
            )
            queryset = queryset.filter(search_filter).distinct()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        limit = request.query_params.get('limit', None)
        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return Response({'error': 'Limit must be a positive integer.'}, status=400)
                queryset = queryset[:limit]
            except ValueError:
                return Response({'error': 'Limit must be an integer.'}, status=400)

        total_count = self.queryset.count()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'total_count': total_count,
            'count': len(serializer.data),
            'results': serializer.data
        })
