from django.contrib import admin
from core.apps.museum.models import EventType
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(EventType)
class EventTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
