from rest_framework import serializers
from core.apps.museum.models import Symbol

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl',
            'image',
            'description_uz', 'description_ru', 'description_en', 'description_uz_Cyrl'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define name and description fields
        name_fields = {
            'name_uz': representation.get('name_uz'),
            'name_ru': representation.get('name_ru'),
            'name_en': representation.get('name_en'),
            'name_uz_Cyrl': representation.get('name_uz_Cyrl')
        }

        description_fields = {
            'description_uz': representation.get('description_uz'),
            'description_ru': representation.get('description_ru'),
            'description_en': representation.get('description_en'),
            'description_uz_Cyrl': representation.get('description_uz_Cyrl')
        }

        # Find the first available non-null and non-empty name
        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        # Find the first available non-null and non-empty description
        available_description = next((desc for desc in description_fields.values() if desc not in (None, '')), '')

        # Update name fields with available name if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        # Update description fields with available description if they are null or empty
        for field in description_fields.keys():
            if not representation.get(field):
                representation[field] = available_description

        return representation
