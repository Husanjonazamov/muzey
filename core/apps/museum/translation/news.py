from modeltranslation.translator import TranslationOptions, register

from core.apps.museum.models import News, NewsType


@register(NewsType)
class NewsTypeTranslationOptions(TranslationOptions):
    fields = ('name',  )


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )
