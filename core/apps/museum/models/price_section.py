from django.db import models
from django.utils.translation import gettext_lazy as _

class PriceSection(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Narx bo'limi")
        verbose_name_plural = _("Narx bo'limlari")


class PriceItem(models.Model):
    description = models.CharField(max_length=255, verbose_name=_("Tavsif"))
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Miqdor"))
    price = models.CharField(max_length=255, verbose_name=_("Narx"))
    section = models.ForeignKey(PriceSection, related_name='items', on_delete=models.CASCADE, verbose_name=_("Bo'lim"))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("Narx elementi")
        verbose_name_plural = _("Narx elementlari")



class PriceText(models.Model):
    text = models.TextField(verbose_name=_("Matn"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Narx matni")
        verbose_name_plural = _("Narx matnlari")