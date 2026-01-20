from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.museum.forms import SymbolAdminForm
from core.apps.museum.models import Symbol
from unfold.admin import ModelAdmin

@admin.register(Symbol)
class SymbolAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'image', 'description')
    search_fields = ('name', 'description')
    form = SymbolAdminForm
