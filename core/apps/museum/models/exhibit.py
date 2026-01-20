from django.db import models
from core.apps.museum.models import image
from core.apps.museum.models.exhibit_type import ExhibitType
from django.utils.translation import gettext_lazy as _

from core.http.models.base import AbstractBaseModel


class Exhibit(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))
    description = models.TextField(verbose_name=_("Tavsif"))
    image = models.ManyToManyField(image.Image, verbose_name=_("Rasm(lar)"))
    material = models.CharField(max_length=255, verbose_name=_("Material"))
    color = models.CharField(max_length=255, verbose_name=_("Rang"))
    type = models.ForeignKey(ExhibitType, on_delete=models.PROTECT, verbose_name=_("Turi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Eksponat")
        verbose_name_plural = _("Eksponatlar")
