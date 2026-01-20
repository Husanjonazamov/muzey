from django.contrib import admin
from core.apps.museum.models import Gallery
from unfold.admin import ModelAdmin


@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ('id', )
    filter_horizontal = ('image', )
