# Generated by Django 3.2 on 2021-06-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0023_auto_20210615_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='technical_info',
            name='phd_spec',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='technical_info',
            name='year_pg',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='technical_info',
            name='year_ug',
            field=models.CharField(default='', max_length=100),
        ),
    ]