# Generated by Django 4.0.2 on 2022-02-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('firstname', models.CharField(max_length=100, unique=True)),
                ('lastname', models.CharField(max_length=150)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is super')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
