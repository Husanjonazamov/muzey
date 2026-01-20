from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import PriceSection, PriceItem, PriceText


@register(PriceSection)
class PriceSectionTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PriceItem)
class PriceItemTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(PriceText)
class PriceTextTranslationOptions(TranslationOptions):
    fields = ('text',)
