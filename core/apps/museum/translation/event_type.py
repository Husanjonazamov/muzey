from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import EventType


@register(EventType)
class EventTypeTranslationOptions(TranslationOptions):
    fields = ("name",)
