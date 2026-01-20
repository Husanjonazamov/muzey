from django.db import models
from django.utils.translation import gettext_lazy as _

class Symbol(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))
    image = models.ImageField(upload_to='symbols/', verbose_name=_("Rasm"))
    description = models.TextField(verbose_name=_("Tavsif"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Davlat ramzi")
        verbose_name_plural = _("Davlat ramzlari")
