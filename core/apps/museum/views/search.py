from rest_framework import views, status
from rest_framework import response
from django.db.models import Q
from core.apps.museum import serializers
from core.apps.museum import models

class UnifiedSearchView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = serializers.SearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        query = serializer.validated_data.get("query", "")

        if not query:
            return response.Response([], status=status.HTTP_200_OK)

        exhibit_results = models.Exhibit.objects.filter(
            Q(name_uz__icontains=query) |
            Q(name_ru__icontains=query) |
            Q(name_en__icontains=query) |
            Q(name_uz_Cyrl__icontains=query)
        )

        management_results = models.Management.objects.filter(
            Q(full_name_uz__icontains=query) |
            Q(full_name_ru__icontains=query) |
            Q(full_name_en__icontains=query) |
            Q(full_name_uz_Cyrl__icontains=query) |
            Q(position_uz__icontains=query) |
            Q(position_ru__icontains=query) |
            Q(position_en__icontains=query) |
            Q(position_uz_Cyrl__icontains=query)
        )

        product_results = models.Product.objects.filter(
            Q(name_uz__icontains=query) |
            Q(name_ru__icontains=query) |
            Q(name_en__icontains=query) |
            Q(name_uz_Cyrl__icontains=query)
        )

        news_results = models.News.objects.filter(
            Q(title_uz__icontains=query) |
            Q(title_ru__icontains=query) |
            Q(title_en__icontains=query) |
            Q(title_uz_Cyrl__icontains=query)
        )

        events_results = models.Events.objects.filter(
            Q(theme_uz__icontains=query) |
            Q(theme_ru__icontains=query) |
            Q(theme_en__icontains=query) |
            Q(theme_uz_Cyrl__icontains=query)
        )

        # Serialize results and add type to each object
        def add_type_field(data, object_type):
            for item in data:
                item["type_class"] = object_type
            return data

        exhibit_serializer = serializers.ShortExhibitSerializer(exhibit_results, many=True)
        management_serializer = serializers.ShortManagementSerializer(management_results, many=True)
        product_serializer = serializers.ShortProductSerializer(product_results, many=True)
        news_serializer = serializers.ShortNewsSerializer(news_results, many=True)
        events_serializer = serializers.ShortEventsSerializer(events_results, many=True)

        # Combine all results into a single list with type information
        results = (
            add_type_field(exhibit_serializer.data, "exhibit") +
            add_type_field(management_serializer.data, "management") +
            add_type_field(product_serializer.data, "product") +
            add_type_field(news_serializer.data, "news") +
            add_type_field(events_serializer.data, "event")
        )

        return response.Response({"results": results}, status=status.HTTP_200_OK)
