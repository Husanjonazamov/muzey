from rest_framework import serializers
from core.apps.museum.models import Exhibit
from core.apps.museum.serializers.image import ImageSerializer

class ExhibitSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, source='image')

    class Meta:
        model = Exhibit
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl',
            'description_uz', 'description_ru', 'description_en', 'description_uz_Cyrl',
            'images',
            'material_uz', 'material_ru', 'material_en', 'material_uz_Cyrl',
            'color_uz', 'color_ru', 'color_en', 'color_uz_Cyrl',
            'type',
            'created_at'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define name, description, material, color, and size fields
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

        material_fields = {
            'material_uz': representation.get('material_uz'),
            'material_ru': representation.get('material_ru'),
            'material_en': representation.get('material_en'),
            'material_uz_Cyrl': representation.get('material_uz_Cyrl')
        }

        color_fields = {
            'color_uz': representation.get('color_uz'),
            'color_ru': representation.get('color_ru'),
            'color_en': representation.get('color_en'),
            'color_uz_Cyrl': representation.get('color_uz_Cyrl')
        }



        # Find the first available non-null and non-empty values
        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')
        available_description = next((desc for desc in description_fields.values() if desc not in (None, '')), '')
        available_material = next((mat for mat in material_fields.values() if mat not in (None, '')), '')
        available_color = next((col for col in color_fields.values() if col not in (None, '')), '')

        # Update name, description, material, color, and size fields with available values if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        for field in description_fields.keys():
            if not representation.get(field):
                representation[field] = available_description

        for field in material_fields.keys():
            if not representation.get(field):
                representation[field] = available_material

        for field in color_fields.keys():
            if not representation.get(field):
                representation[field] = available_color



        return representation


class ShortExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Define name and description fields
        name_fields = {
            'name_uz': representation.get('name_uz'),
            'name_ru': representation.get('name_ru'),
            'name_en': representation.get('name_en'),
            'name_uz_Cyrl': representation.get('name_uz_Cyrl')
        }


        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        # Update name and description fields with available values if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name


        return representation
