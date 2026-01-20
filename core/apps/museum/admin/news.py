from django.contrib import admin

from core.apps.museum.forms import NewsAdminForm
from core.apps.museum.models.news import News, NewsType
from core.apps.museum.models.image import Image
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin



@admin.register(NewsType)
class NewsTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)


@admin.register(News)
class NewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'text',)
    search_fields = ('text', )
    form = NewsAdminForm
    filter_horizontal = ('image',)

@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('image',)
