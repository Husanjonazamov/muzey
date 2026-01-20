from datetime import datetime
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.apps.museum.models import Events
from core.apps.museum.serializers import EventsSerializer


class EventsListView(ListAPIView):
    serializer_class = EventsSerializer

    def get_queryset(self):
        queryset = Events.objects.all().order_by('-created_at')

        date_str = self.request.query_params.get('date', None)
        if date_str:
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                queryset = queryset.filter(date__date=date)
            except ValueError:
                return Events.objects.none()

        type_id_str = self.request.query_params.get('type', None)
        if type_id_str:
            try:
                type_id = int(type_id_str)
                queryset = queryset.filter(type_id=type_id)
            except ValueError:
                return Events.objects.none()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        total_count = queryset.count()

        limit_str = request.query_params.get('limit', None)
        if limit_str:
            try:
                limit = int(limit_str)
                if limit > 0:
                    queryset = queryset[:limit]
                else:
                    return Response({'error': 'Limit must be a positive integer'}, status=400)
            except ValueError:
                return Response({'error': 'Limit must be an integer'}, status=400)

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'total_count': total_count,
            'count': len(serializer.data),
            'results': serializer.data
        })
class EventDetailView(RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    lookup_field = 'id'