from django.contrib import admin
from core.apps.museum.models import Connect
from unfold.admin import ModelAdmin


@admin.register(Connect)
class ConnectAdmin(ModelAdmin):
    list_display = ('user_name', 'phone', 'massage')
    search_fields = ('user_name', 'phone')
