# Generated by Django 5.1.6 on 2025-02-24 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_imagepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='userId',
        ),
    ]
