from django.contrib import admin
from core.apps.museum.models import SocialMedia
from unfold.admin import ModelAdmin


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin):
    list_display = ('id', 'url')
