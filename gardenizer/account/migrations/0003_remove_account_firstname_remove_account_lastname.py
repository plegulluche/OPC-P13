# Generated by Django 4.0.2 on 2022-03-01 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_account_username_alter_account_firstname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="firstname",
        ),
        migrations.RemoveField(
            model_name="account",
            name="lastname",
        ),
    ]
