from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import Symbol

@register(Symbol)
class SymbolTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
