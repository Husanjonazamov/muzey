from django.db import models
from django.utils.translation import gettext_lazy as _

class SocialMedia(models.Model):
    url = models.URLField(verbose_name=_("URL"))
    icon = models.ImageField(upload_to='social_icons/', blank=True, null=True, verbose_name=_("Ikonka"))

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _("Ijtimoiy tarmoq")
        verbose_name_plural = _("Ijtimoiy tarmoqlar")
