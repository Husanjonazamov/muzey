from rest_framework import serializers
from core.apps.museum.models import VideoGallery

class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = [
            'id',
            'video_url',
            'title_uz', 'title_ru', 'title_en', 'title_uz_Cyrl',
            'text_uz', 'text_ru', 'text_en', 'text_uz_Cyrl',
            'image'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define title and text fields
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

        # Find the first available non-null and non-empty title
        available_title = next((title for title in title_fields.values() if title not in (None, '')), '')

        # Find the first available non-null and non-empty text
        available_text = next((text for text in text_fields.values() if text not in (None, '')), '')

        # Update title fields with available title if they are null or empty
        for field in title_fields.keys():
            if not representation.get(field):
                representation[field] = available_title

        # Update text fields with available text if they are null or empty
        for field in text_fields.keys():
            if not representation.get(field):
                representation[field] = available_text

        return representation
