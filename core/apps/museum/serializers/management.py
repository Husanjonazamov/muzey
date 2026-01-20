from rest_framework import serializers
from core.apps.museum.models import Management, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["phone"]


class ManagementSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)

    class Meta:
        model = Management
        fields = [
            'id',
            'full_name_uz', 'full_name_ru', 'full_name_en', 'full_name_uz_Cyrl',
            'position_uz', 'position_ru', 'position_en', 'position_uz_Cyrl',
            'image',
            'phone',
            'email'
        ]

    def to_representation(self, instance):
        # Get the default representation
        representation = super().to_representation(instance)

        # Define name fields
        full_name_fields = {
            'full_name_uz': representation.get('full_name_uz'),
            'full_name_ru': representation.get('full_name_ru'),
            'full_name_en': representation.get('full_name_en'),
            'full_name_uz_Cyrl': representation.get('full_name_uz_Cyrl')
        }

        # Define position fields
        position_fields = {
            'position_uz': representation.get('position_uz'),
            'position_ru': representation.get('position_ru'),
            'position_en': representation.get('position_en'),
            'position_uz_Cyrl': representation.get('position_uz_Cyrl')
        }



        # Find the first available non-null and non-empty full_name
        available_full_name = next((name for name in full_name_fields.values() if name not in (None, '')), '')

        # Find the first available non-null and non-empty position
        available_position = next((pos for pos in position_fields.values() if pos not in (None, '')), '')

        # Find the first available non-null and non-empty description

        # Update full_name fields with available full_name if they are null or empty
        for field in full_name_fields.keys():
            if not representation.get(field):
                representation[field] = available_full_name

        for field in position_fields.keys():
            if not representation.get(field):
                representation[field] = available_position

        return representation



class ShortManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'full_name_uz', 'full_name_ru', 'full_name_en', 'full_name_uz_Cyrl']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        name_fields = {
            'name_uz': representation.pop('full_name_uz'),
            'name_ru': representation.pop('full_name_ru'),
            'name_en': representation.pop('full_name_en'),
            'name_uz_Cyrl': representation.pop('full_name_uz_Cyrl')
        }

        available_name = next((name for name in name_fields.values() if name not in (None, '')), '')

        for field, value in name_fields.items():
            representation[field] = value if value else available_name

        return representation
