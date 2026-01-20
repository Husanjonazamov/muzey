from django.contrib import admin

from core.apps.museum.models import Exhibit
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Exhibit)
class ExhibitAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('name', 'description', 'type', 'material')
    search_fields = ('name',)
    filter_horizontal = ('image',)

