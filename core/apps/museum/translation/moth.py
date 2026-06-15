from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import Moth, MothType


@register(MothType)
class MothTypeTranslationOptions(TranslationOptions):
    fields = ('name',  )


@register(Moth)
class MothTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )
