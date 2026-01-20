from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.museum.models import Image
from core.apps.museum.models.event_type import EventType
from core.http.models.base import AbstractBaseModel


class Events(AbstractBaseModel):
    theme = models.CharField(max_length=300, verbose_name=_("Mavzu"))
    description = models.TextField(verbose_name=_("Tavsif"))
    image = models.ManyToManyField(Image, verbose_name=_("Rasm(lar)"))
    date = models.DateTimeField(verbose_name=_("Sana"))
    type = models.ForeignKey(EventType, on_delete=models.PROTECT, verbose_name=_("Turi"))

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = _("Tadbir")
        verbose_name_plural = _("Tadbirlar")
