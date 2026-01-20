from rest_framework import serializers
from core.apps.museum.models import Product, ProductType



class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl'
        ]

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

        # Update name fields with available name if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        return representation



class ProductSerializer(serializers.ModelSerializer):
    type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl',
            'image',
            'desc_uz', 'desc_ru', 'desc_en', 'desc_uz_Cyrl',
            'price',
            'type',
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

        desc_fields = {
            'desc_uz': representation.get('desc_uz'),
            'desc_ru': representation.get('desc_ru'),
            'desc_en': representation.get('desc_en'),
            'desc_uz_Cyrl': representation.get('desc_uz_Cyrl')
        }

        # Find the first available non-null and non-empty name
        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        # Find the first available non-null and non-empty description
        available_desc = next((desc for desc in desc_fields.values() if desc not in (None, '')), '')

        # Update name fields with available name if they are null or empty
        for field in name_fields.keys():
            if not representation.get(field):
                representation[field] = available_name

        # Update description fields with available description if they are null or empty
        for field in desc_fields.keys():
            if not representation.get(field):
                representation[field] = available_desc

        return representation


class ShortProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name_uz', 'name_ru', 'name_en', 'name_uz_Cyrl',

                    ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

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