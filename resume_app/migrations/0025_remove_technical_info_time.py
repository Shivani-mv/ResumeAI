# Generated by Django 3.2 on 2021-06-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0024_auto_20210616_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technical_info',
            name='time',
        ),
    ]