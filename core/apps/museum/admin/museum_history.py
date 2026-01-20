from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from core.apps.museum.forms.museum_history import MuseumHistoryForm
from core.apps.museum.models import MuseumHistory


@admin.register(MuseumHistory)
class MuseumHistoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    form = MuseumHistoryForm
    list_display = ('text',)

