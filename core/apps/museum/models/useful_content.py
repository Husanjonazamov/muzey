from django.db import models
from django.utils.translation import gettext_lazy as _

class UsefulContent(models.Model):
    image = models.ImageField(upload_to='useful_content_images/', verbose_name=_("Rasm"))
    definition = models.TextField(verbose_name=_("Tavsif"))
    url = models.URLField(max_length=200, verbose_name=_("URL"))
    url_name = models.CharField(max_length=255, verbose_name=_("URL nomi"))

    def __str__(self):
        return self.url_name

    class Meta:
        verbose_name = _("Foydali kontent")
        verbose_name_plural = _("Foydali kontentlar")
