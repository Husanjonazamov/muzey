import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("museum", "0039_remove_management_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MothType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Nomi")),
                ("name_uz", models.CharField(max_length=200, null=True)),
                ("name_uz_Cyrl", models.CharField(max_length=200, null=True)),
                ("name_ru", models.CharField(max_length=200, null=True)),
                ("name_en", models.CharField(max_length=200, null=True)),
            ],
            options={
                "verbose_name": "Moth turi",
                "verbose_name_plural": "Moth turlari",
            },
        ),
        migrations.CreateModel(
            name="Moth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Sarlavha")),
                ("title_uz", models.CharField(max_length=255, null=True)),
                ("title_uz_Cyrl", models.CharField(max_length=255, null=True)),
                ("title_ru", models.CharField(max_length=255, null=True)),
                ("title_en", models.CharField(max_length=255, null=True)),
                ("text", models.TextField(verbose_name="Matn")),
                ("text_uz", models.TextField(null=True)),
                ("text_uz_Cyrl", models.TextField(null=True)),
                ("text_ru", models.TextField(null=True)),
                ("text_en", models.TextField(null=True)),
                ("date", models.DateTimeField(blank=True, null=True)),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="museum.mothtype",
                        verbose_name="Turi",
                    ),
                ),
                (
                    "image",
                    models.ManyToManyField(
                        to="museum.image", verbose_name="Rasm(lar)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Moth",
                "verbose_name_plural": "Mothlar",
            },
        ),
    ]
