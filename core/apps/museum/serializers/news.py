import re

from rest_framework import serializers
from core.apps.museum.models import News, NewsType
from core.apps.museum.serializers.image import ImageSerializer

class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Define name fields
        name_fields = {
            'name_uz': representation.get('name_uz'),
            'name_ru': representation.get('name_ru'),
            'name_en': representation.get('name_en'),
            'name_uz_Cyrl': representation.get('name_uz_Cyrl')
        }

        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        return representation


class NewsSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'title_uz_Cyrl',
                  'image', 'text_uz', 'text_ru', 'text_en', 'text_uz_Cyrl',
                  'created_at', 'type', 'date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Define the base URL
        base_url = "https://muzey.felixits.uz"

        title_fields = {
            'title_uz': representation.get('title_uz'),
            'title_ru': representation.get('title_ru'),
            'title_en': representation.get('title_en'),
            'title_uz_Cyrl': representation.get('title_uz_Cyrl')
        }

        text_fields = {
            'text_uz': representation.get('text_uz'),
            'text_ru': representation.get('text_ru'),
            'text_en': representation.get('text_en'),
            'text_uz_Cyrl': representation.get('text_uz_Cyrl')
        }

        available_title = next((title for title in title_fields.values() if title not in (None, '')), '')

        for field in title_fields.keys():
            if not representation.get(field):
                representation[field] = available_title

        available_text = next((text for text in text_fields.values() if text not in (None, '')), '')

        for field in text_fields.keys():
            if not representation.get(field):
                representation[field] = available_text

            if representation.get(field):
                clean_text = representation[field].replace('\\', '/').rstrip('/')
                clean_text = re.sub(
                    r'src=\"(/media/[^"]+)\"',
                    f'src=\"{base_url}\\1\"',
                    clean_text
                )
                representation[field] = clean_text

        return representation

class ShortNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title_uz', 'title_ru', 'title_en', 'title_uz_Cyrl', 'date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        name_fields = {
            'name_uz': representation.pop('title_uz'),
            'name_ru': representation.pop('title_ru'),
            'name_en': representation.pop('title_en'),
            'name_uz_Cyrl': representation.pop('title_uz_Cyrl')
        }

        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        for field, value in name_fields.items():
            representation[field] = value if value else available_name

        return representation
