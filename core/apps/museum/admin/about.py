from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.museum.forms import ExhibitAdminForm
from core.apps.museum.models import About, Address, Location
from unfold.admin import ModelAdmin

@admin.register(About)
class AboutAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'title', 'email')
    search_fields = ('title', 'phone', 'email')
    form = ExhibitAdminForm
    filter_horizontal = ('phone',)


@admin.register(Address)
class AddressAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'region', 'district', 'street', 'home')
    search_fields = ('region', 'district', 'street', 'home')



@admin.register(Location)
class LocationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'address', 'latitude', 'longitude')
    search_fields = ('name', 'address__region', 'latitude', 'longitude')
