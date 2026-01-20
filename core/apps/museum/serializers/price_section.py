from rest_framework import serializers
from core.apps.museum.models import PriceSection, PriceItem, PriceText


class PriceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceItem
        fields = [
            'id',
            'description_uz', 'description_ru', 'description_en', 'description_uz_Cyrl',
            'quantity',
            'price'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define description fields
        description_fields = {
            'description_uz': representation.get('description_uz'),
            'description_ru': representation.get('description_ru'),
            'description_en': representation.get('description_en'),
            'description_uz_Cyrl': representation.get('description_uz_Cyrl')
        }

        # Find the first available non-null and non-empty description
        available_description = next((desc for desc in description_fields.values() if desc not in (None, '')), '')

        # Update description fields with available description if they are null or empty
        for field in description_fields.keys():
            if not representation.get(field):
                representation[field] = available_description

        return representation

class PriceSectionSerializer(serializers.ModelSerializer):
    items = PriceItemSerializer(many=True)

    class Meta:
        model = PriceSection
        fields = [
            'id',
            'title_uz', 'title_ru', 'title_en', 'title_uz_Cyrl',
            'items'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define title fields
        title_fields = {
            'title_uz': representation.get('title_uz'),
            'title_ru': representation.get('title_ru'),
            'title_en': representation.get('title_en'),
            'title_uz_Cyrl': representation.get('title_uz_Cyrl')
        }

        # Find the first available non-null and non-empty title
        available_title = next((title for title in title_fields.values() if title not in (None, '')), '')

        # Update title fields with available title if they are null or empty
        for field in title_fields.keys():
            if not representation.get(field):
                representation[field] = available_title

        return representation


class PriceTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceText
        fields = [
            'id',
            'text_uz', 'text_ru', 'text_en', 'text_uz_Cyrl'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define text fields in multiple languages
        text_fields = {
            'text_uz': representation.get('text_uz'),
            'text_ru': representation.get('text_ru'),
            'text_en': representation.get('text_en'),
            'text_uz_Cyrl': representation.get('text_uz_Cyrl')
        }

        # Find the first available non-null and non-empty text
        available_text = next((text for text in text_fields.values() if text not in (None, '')), '')

        # Update text fields with available text if they are null or empty
        for field in text_fields.keys():
            if not representation.get(field):
                representation[field] = available_text

        return representation
