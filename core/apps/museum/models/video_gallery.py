from django.db import models
from django.utils.translation import gettext_lazy as _

class VideoGallery(models.Model):
    video_url = models.URLField(verbose_name=_("Video URL"))
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    text = models.TextField(verbose_name=_("Matn"))
    image = models.ImageField(upload_to="video_image/", null=True, blank=True, verbose_name=_("Rasm"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Video galereya")
        verbose_name_plural = _("Video galereyalar")
