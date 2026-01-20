from django.db import models
from core.apps.museum.models import image
from django.utils.translation import gettext_lazy as _

from core.http.models.base import AbstractBaseModel

class NewsType(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nomi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Yangilik turi")
        verbose_name_plural = _("Yangilik turlari")


class News(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    text = models.TextField(verbose_name=_("Matn"))
    image = models.ManyToManyField(image.Image, verbose_name=_("Rasm(lar)"))
    type = models.ForeignKey(NewsType, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Turi"))
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = _("Yangilik")
        verbose_name_plural = _("Yangiliklar")
