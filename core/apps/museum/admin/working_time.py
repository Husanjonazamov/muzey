from django.contrib import admin
from core.apps.museum.models import WorkingTime
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(WorkingTime)
class WorkingTimeAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('weekday', 'start_time', 'end_time')
    search_fields = ('weekday',)


