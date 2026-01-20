from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import UsefulContent

@register(UsefulContent)
class UsefulContentTranslationOptions(TranslationOptions):
    fields = ('definition',)
