from django.db import models
from core.http.models.base import AbstractBaseModel
from django.utils.translation import gettext_lazy as _

class MuseumHistory(AbstractBaseModel):
    text = models.TextField(verbose_name=_("Matn"))

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = _("Muzey tarixi")
        verbose_name_plural = _("Muzey tarixlari")