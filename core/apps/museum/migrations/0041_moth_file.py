from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("museum", "0040_mothtype_moth"),
    ]

    operations = [
        migrations.AddField(
            model_name="moth",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="moth_files",
                verbose_name="Fayl",
            ),
        ),
    ]
