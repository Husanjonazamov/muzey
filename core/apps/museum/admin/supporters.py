from django.contrib import admin
from unfold.admin import ModelAdmin
from core.apps.museum.models import Supporters

@admin.register(Supporters)
class SupportersAdmin(ModelAdmin):
    fields = ('logo', )