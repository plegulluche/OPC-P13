# Generated by Django 4.0.2 on 2022-02-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="username",
            field=models.CharField(default="", max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="firstname",
            field=models.CharField(max_length=100),
        ),
    ]
