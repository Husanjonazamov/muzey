from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import ExhibitType


@register(ExhibitType)
class ExhibitTypeTranslationOptions(TranslationOptions):
    fields = ("name",)
