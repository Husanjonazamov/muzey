from rest_framework import serializers
from core.apps.museum.models import ExhibitType

class ExhibitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitType
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define name fields
        name_fields = {
            'name_uz': representation.get('name_uz'),
            'name_ru': representation.get('name_ru'),
            'name_en': representation.get('name_en'),
            'name_uz_Cyrl': representation.get('name_uz_Cyrl')
        }

        # Find the first available non-null and non-empty name
        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        # Update name fields with available name if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        return representation
