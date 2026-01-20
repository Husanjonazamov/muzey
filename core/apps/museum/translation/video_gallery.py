from modeltranslation.translator import TranslationOptions, register
from core.apps.museum.models import VideoGallery

@register(VideoGallery)
class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
