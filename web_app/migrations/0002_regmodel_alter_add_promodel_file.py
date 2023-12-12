# Generated by Django 4.2.1 on 2023-10-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Regmodel",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=50)),
                ("pincode", models.IntegerField()),
                ("phone", models.IntegerField()),
                ("password", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="add_promodel",
            name="file",
            field=models.FileField(upload_to="web_app/static"),
        ),
    ]