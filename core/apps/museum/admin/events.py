from django.contrib import admin

from core.apps.museum.forms import EventsAdminForm
from core.apps.museum.models import  Events
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Events)
class EventsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'theme', 'description', 'type')
    search_fields = ('theme', 'date')
    form = EventsAdminForm
    filter_horizontal = ('image',)