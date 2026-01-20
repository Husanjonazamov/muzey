from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import WorkingTime

@register(WorkingTime)
class WorkingTimeTranslationOptions(TranslationOptions):
    fields = ('weekday',)
