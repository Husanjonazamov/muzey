from django.db import models
from django.utils.translation import gettext_lazy as _

from core.http.models.base import AbstractBaseModel


class EventType(AbstractBaseModel):
    name = models.CharField(max_length=300, verbose_name=_("Nomi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tadbir turi")
        verbose_name_plural = _("Tadbir turlari")