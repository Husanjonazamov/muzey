from django.db import models
from core.http.models.base import AbstractBaseModel
from django.utils.translation import gettext_lazy as _

class ExhibitType(AbstractBaseModel):
    name = models.CharField(max_length=300, verbose_name=_("Nomi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Eksponat turi")
        verbose_name_plural = _("Eksponat turlari")
