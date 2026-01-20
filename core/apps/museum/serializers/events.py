from rest_framework import serializers
from core.apps.museum.models import Events
from core.apps.museum.serializers import ImageSerializer
import re

class EventsSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Events
        fields = [
            'id',
            'theme_uz', 'theme_ru', 'theme_en', 'theme_uz_Cyrl',
            'description_uz', 'description_ru', 'description_en', 'description_uz_Cyrl',
            'image',
            'date',
            'type',
            'created_at'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        base_url = "https://muzey.felixits.uz"

        # Fields for theme and description translations
        theme_fields = {
            'theme_uz': representation.get('theme_uz'),
            'theme_ru': representation.get('theme_ru'),
            'theme_en': representation.get('theme_en'),
            'theme_uz_Cyrl': representation.get('theme_uz_Cyrl')
        }

        description_fields = {
            'description_uz': representation.get('description_uz'),
            'description_ru': representation.get('description_ru'),
            'description_en': representation.get('description_en'),
            'description_uz_Cyrl': representation.get('description_uz_Cyrl')
        }

        available_theme = next((theme for theme in theme_fields.values() if theme not in (None, '')), '')
        available_description = next((desc for desc in description_fields.values() if desc not in (None, '')), '')

        for field in theme_fields.keys():
            if not representation.get(field):
                representation[field] = available_theme


        for field in description_fields.keys():
            if not representation.get(field):
                representation[field] = available_description

            if representation.get(field):
                clean_description = representation[field].replace('\\', '/').rstrip('/')
                clean_description = re.sub(
                    r'src=\"(/media/[^"]+)\"',
                    f'src=\"{base_url}\\1\"',
                    clean_description
                )
                representation[field] = clean_description

        return representation

class ShortEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'theme_uz', 'theme_ru', 'theme_en', 'theme_uz_Cyrl']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        name_fields = {
            'name_uz': representation.pop('theme_uz'),
            'name_ru': representation.pop('theme_ru'),
            'name_en': representation.pop('theme_en'),
            'name_uz_Cyrl': representation.pop('theme_uz_Cyrl')
        }

        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        for field, value in name_fields.items():
            representation[field] = value if value else available_name

        return representation
