# Generated by Django 4.2.1 on 2023-07-26 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tend", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "catalogo",
                "verbose_name_plural": "Catalogos",
            },
        ),
    ]
