from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import Management


@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', )
