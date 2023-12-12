# Generated by Django 4.2.1 on 2023-10-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="add_promodel",
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
                ("file", models.FileField(upload_to="webapp/static")),
                ("name", models.CharField(max_length=30)),
                ("des", models.CharField(max_length=60)),
                ("pri", models.IntegerField()),
                ("offer", models.CharField(max_length=30)),
            ],
        ),
    ]