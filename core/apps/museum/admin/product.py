from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.museum.models import Product, ProductType
from unfold.admin import ModelAdmin


@admin.register(ProductType)
class ProductTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'price', 'type')
    search_fields = ('name', 'desc')
