from django.contrib import admin
from core.apps.museum.models import ExhibitType
from unfold.admin import ModelAdmin

from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(ExhibitType)
class ExhibitTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
