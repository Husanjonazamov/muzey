from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import Product, ProductType

@register(ProductType)
class ProductTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'desc')
