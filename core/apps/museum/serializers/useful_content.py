from rest_framework import serializers
from core.apps.museum.models import UsefulContent

class UsefulContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulContent
        fields = [
            'id',
            'image',
            'definition_uz', 'definition_ru', 'definition_en', 'definition_uz_Cyrl',
            'url', 'url_name'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define definition fields
        definition_fields = {
            'definition_uz': representation.get('definition_uz'),
            'definition_ru': representation.get('definition_ru'),
            'definition_en': representation.get('definition_en'),
            'definition_uz_Cyrl': representation.get('definition_uz_Cyrl')
        }

        # Find the first available non-null and non-empty definition
        available_definition = next((defn for defn in definition_fields.values() if defn not in (None, '')), '')

        # Update definition fields with available definition if they are null or empty
        for field in definition_fields.keys():
            if not representation.get(field):
                representation[field] = available_definition

        return representation
