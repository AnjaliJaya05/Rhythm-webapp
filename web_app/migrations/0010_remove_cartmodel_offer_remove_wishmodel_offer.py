# Generated by Django 4.2.1 on 2023-10-20 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0009_remove_checkout_proid"),
    ]

    operations = [
        migrations.RemoveField(model_name="cartmodel", name="offer",),
        migrations.RemoveField(model_name="wishmodel", name="offer",),
    ]