from django.contrib import admin
from core.apps.museum.models import Management, Phone
from unfold.admin import ModelAdmin

from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(Phone)
class PhoneAdmin(ModelAdmin):
    list_display = ('phone', )

@admin.register(Management)
class ManagementAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'position')
    search_fields = ('full_name', 'position')
    filter_horizontal = ('phone', )
