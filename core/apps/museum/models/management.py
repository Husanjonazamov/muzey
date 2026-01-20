from click.core import batch
from django.db import models
from django.utils.translation import gettext_lazy as _

class Phone(models.Model):
    phone = models.CharField(max_length=30, verbose_name=_("Telefon"))

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _("Telefon")
        verbose_name_plural = _("Telefonlar")


class Management(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("To'liq ism"))
    position = models.CharField(max_length=255, verbose_name=_("Lavozim"))
    image = models.ImageField(upload_to="team_images", verbose_name=_("Rasm"))
    phone = models.ManyToManyField(Phone, verbose_name=_("Telefon(lar)"))
    email = models.CharField(max_length=100, verbose_name=_("Email"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Boshqaruv")
        verbose_name_plural = _("Boshqaruvchilar")
