from django.db import models

from core.apps.museum.models.management import Phone


from django.db import models
from django.utils.translation import gettext_lazy as _

class About(models.Model):
    image = models.ImageField(upload_to="museum_about", verbose_name=_("Rasm"))
    title = models.CharField(max_length=300, verbose_name=_("Sarlavha"))
    text = models.TextField(verbose_name=_("Matn"))
    phone = models.ManyToManyField("Phone", verbose_name=_("Telefonlar"))
    email = models.CharField(max_length=100, verbose_name=_("Email"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Haqida")
        verbose_name_plural = _("Haqida")



class Address(models.Model):
    region = models.CharField(max_length=100, verbose_name=_("Viloyat"))
    district = models.CharField(max_length=100, verbose_name=_("Tuman"))
    street = models.CharField(max_length=100, verbose_name=_("Ko'cha"))
    home = models.CharField(max_length=100, verbose_name=_("Uy"))

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = _("Manzil")
        verbose_name_plural = _("Manzillar")

class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))
    address = models.ForeignKey("Address", on_delete=models.CASCADE, verbose_name=_("Manzil"))
    latitude = models.FloatField(verbose_name=_("Kenglik"))
    longitude = models.FloatField(verbose_name=_("Uzunlik"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Joylashuv")
        verbose_name_plural = _("Joylashuvlar")