from rest_framework import serializers
from core.apps.museum.models import WorkingTime

class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = ['id', 'weekday_uz', 'weekday_ru', 'weekday_en', 'weekday_uz_Cyrl', 'start_time', 'end_time']

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define weekday fields
        weekday_fields = {
            'weekday_uz': representation.get('weekday_uz'),
            'weekday_ru': representation.get('weekday_ru'),
            'weekday_en': representation.get('weekday_en'),
            'weekday_uz_Cyrl': representation.get('weekday_uz_Cyrl')
        }

        # Find the first available non-null and non-empty weekday
        available_weekday = next((day for day in weekday_fields.values() if day not in (None, '')), '')

        # Update weekday fields with available weekday if they are null or empty
        for field in weekday_fields.keys():
            if not representation.get(field):
                representation[field] = available_weekday

        return representation
