from django.db import models
from django.utils.translation import gettext_lazy as _
from core.http.models.base import AbstractBaseModel



class Connect(AbstractBaseModel):
    user_name = models.CharField(max_length=100, verbose_name=_("Foydalanuvchi nomi"))
    phone = models.CharField(max_length=25, verbose_name=_("Telefon"))
    massage = models.TextField(verbose_name=_("Xabar"))

    def __str__(self) -> str:
        return self.user_name

    class Meta:
        verbose_name = _("Bog'lanish")
        verbose_name_plural = _("Bog'lanishlar")