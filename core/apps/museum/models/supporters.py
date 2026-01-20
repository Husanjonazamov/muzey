from django.db import models
from django.utils.translation import gettext_lazy as _

class Supporters(models.Model):
    logo = models.ImageField(upload_to="museum_supporters", verbose_name=_("Logo"))

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = _("Hamkor")
        verbose_name_plural = _("Hamkorlar")
