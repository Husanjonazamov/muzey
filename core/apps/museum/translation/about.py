from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import About, Address, Location

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('region', 'district', 'street', 'home')

@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('name',)