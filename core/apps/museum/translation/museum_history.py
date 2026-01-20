from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import MuseumHistory


@register(MuseumHistory)
class MuseumHistoryTranslationOptions(TranslationOptions):
    fields = ('text', )
