from django.contrib import admin

from core.apps.museum.forms import PriceTextAdminForm
from core.apps.museum.models import PriceSection, PriceItem, PriceText
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(PriceSection)
class PriceSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(PriceItem)
class PriceItemAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('quantity', 'price', 'section')
    search_fields = ('description', 'price')

@admin.register(PriceText)
class PriceTextAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('text',)
    search_fields = ('text',)
    form = PriceTextAdminForm

