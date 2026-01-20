from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.museum.models import VideoGallery
from unfold.admin import ModelAdmin


@admin.register(VideoGallery)
class VideoGalleryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'video_url', 'title', 'text')
    search_fields = ('title', 'text')
