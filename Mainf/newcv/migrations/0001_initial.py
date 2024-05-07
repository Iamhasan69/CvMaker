# Generated by Django 5.0.4 on 2024-05-07 09:18

import django_mysql.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVINFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('contc_info', models.CharField(max_length=90)),
                ('email_info', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=120)),
                ('profile_summary', models.TextField()),
                ('education', models.CharField(max_length=200)),
                ('skills', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=10, size=None)),
                ('projects', django_mysql.models.ListTextField(models.CharField(max_length=225), size=None)),
                ('other_info', models.TextField()),
            ],
        ),
    ]