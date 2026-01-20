from django.contrib import admin
from core.apps.museum.models import UsefulContent
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(UsefulContent)
class UsefulContentAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('url_name', 'definition', )
    search_fields = ('url_name', 'definition', 'url')

