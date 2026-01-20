from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.museum.models import Image
from core.http.models.base import AbstractBaseModel


class Gallery(AbstractBaseModel):
    image = models.ManyToManyField(Image, verbose_name=_("Rasm(lar)"))
    name = models.CharField(max_length=255, verbose_name=_("Nomi"), null=True, blank=True)

    def __str__(self) -> str:
        if str:
            return str(self.name)
        first_image = (self.image.first())
        if str(first_image) and str(first_image.name):
            return str(first_image.name)
        return "Gallery"

    class Meta:
        verbose_name = _("Galereya")
        verbose_name_plural = _("Galereyalar")
