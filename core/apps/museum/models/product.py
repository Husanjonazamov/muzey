from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Mahsulot turi")
        verbose_name_plural = _("Mahsulot turlari")


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nomi"))
    image = models.ImageField(upload_to='products/', verbose_name=_("Rasm"))
    desc = models.TextField(verbose_name=_("Tavsif"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narx"))
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products', verbose_name=_("Turi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")
