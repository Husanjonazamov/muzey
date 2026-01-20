from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import Events


@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('theme', 'description',)
