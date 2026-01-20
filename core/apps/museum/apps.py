from django.apps import AppConfig


class MuseumConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.museum"

    # def ready(self):
    #     import core.apps.museum.translation
