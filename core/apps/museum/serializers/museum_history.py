from rest_framework import serializers
from core.apps.museum.models import MuseumHistory
import re

class MuseumHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MuseumHistory
        fields = ('id', 'text_uz', 'text_ru', 'text_en', 'text_uz_Cyrl')

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define the base URL
        base_url = "https://muzey.felixits.uz"

        # Define text fields
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

            # Add base URL to the src attribute in text fields and replace backslashes with forward slashes
            if representation.get(field):
                # Replace backslashes with forward slashes and remove any trailing backslashes
                clean_text = representation[field].replace('\\', '/').rstrip('/')

                # Update the src attribute with the base URL
                clean_text = re.sub(
                    r'src=\"(/media/[^"]+)\"',
                    f'src=\"{base_url}\\1\"',
                    clean_text
                )

                # Update the representation with the cleaned text
                representation[field] = clean_text

        return representation
