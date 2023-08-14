# Generated by Django 4.2.1 on 2023-07-26 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                ("description", models.TextField(verbose_name="Descripción")),
                (
                    "image",
                    models.ImageField(upload_to="projects", verbose_name="Imagen"),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Dirección Web"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de edición"
                    ),
                ),
            ],
            options={
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
                "ordering": ["-created"],
            },
        ),
    ]
