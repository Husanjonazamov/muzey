from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import Exhibit


@register(Exhibit)
class ExhibitTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'material', 'color', )
