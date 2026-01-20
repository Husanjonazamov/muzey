from django.db import models
from django.utils.translation import gettext_lazy as _

class WorkingTime(models.Model):
    weekday = models.CharField(max_length=30, verbose_name=_("Hafta kuni"))
    start_time = models.TimeField(verbose_name=_("Boshlanish vaqti"))
    end_time = models.TimeField(verbose_name=_("Tugash vaqti"))

    def __str__(self):
        return self.weekday

    class Meta:
        verbose_name = _("Ish vaqti")
        verbose_name_plural = _("Ish vaqtlar")
        ordering = ['weekday']
