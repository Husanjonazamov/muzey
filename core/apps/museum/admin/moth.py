from django.contrib import admin

from core.apps.museum.forms import MothAdminForm
from core.apps.museum.models.moth import Moth, MothType
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin



@admin.register(MothType)
class MothTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)


@admin.register(Moth)
class MothAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'text',)
    search_fields = ('text', )
    form = MothAdminForm
    filter_horizontal = ('image',)
