from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models.base import AbstractBaseModel


class Image(AbstractBaseModel):
    image = models.ImageField(upload_to="museum_images", verbose_name=_("Rasm"))
    name = models.CharField(max_length=255, verbose_name=_("Nomi"), null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name) or str(self.image.name) if str(self.image) else "Image"

    class Meta:
        verbose_name = _("Rasm")
        verbose_name_plural = _("Rasmlar")
