from rest_framework import serializers
from core.apps.museum.models.about import About, Address, Location
from core.apps.museum.serializers.management import PhoneSerializer
import re


class AboutSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)

    class Meta:
        model = About
        fields = [
            'id',
            'image',
            'title_uz', 'title_ru', 'title_en', 'title_uz_Cyrl',
            'text_uz', 'text_ru', 'text_en', 'text_uz_Cyrl',
            'phone',
            'email'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define the base URL
        base_url = "https://muzey.felixits.uz"

        # Define text fields for titles and content
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

        # Update title fields with available title if they are null or empty
        for field in title_fields.keys():
            if not representation.get(field):
                representation[field] = available_title

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

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'region_uz', 'region_ru', 'region_en', 'region_uz_Cyrl',
            'district_uz', 'district_ru', 'district_en', 'district_uz_Cyrl',
            'street_uz', 'street_ru', 'street_en', 'street_uz_Cyrl',
            'home_uz', 'home_ru', 'home_en', 'home_uz_Cyrl'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define address fields
        address_fields = {
            'region_uz': representation.get('region_uz'),
            'region_ru': representation.get('region_ru'),
            'region_en': representation.get('region_en'),
            'region_uz_Cyrl': representation.get('region_uz_Cyrl'),
            'district_uz': representation.get('district_uz'),
            'district_ru': representation.get('district_ru'),
            'district_en': representation.get('district_en'),
            'district_uz_Cyrl': representation.get('district_uz_Cyrl'),
            'street_uz': representation.get('street_uz'),
            'street_ru': representation.get('street_ru'),
            'street_en': representation.get('street_en'),
            'street_uz_Cyrl': representation.get('street_uz_Cyrl'),
            'home_uz': representation.get('home_uz'),
            'home_ru': representation.get('home_ru'),
            'home_en': representation.get('home_en'),
            'home_uz_Cyrl': representation.get('home_uz_Cyrl'),
        }

        # Find the first available non-null and non-empty address
        available_address = next((address for address in address_fields.values() if address not in (None, '')), '')

        # Update address fields with available address if they are null or empty
        for field in address_fields.keys():
            if not representation.get(field):
                representation[field] = available_address

        return representation



class LocationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Location
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl',
            'address',
            'latitude',
            'longitude'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define location fields
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