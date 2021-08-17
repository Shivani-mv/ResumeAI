# Generated by Django 3.2 on 2021-06-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0022_auto_20210615_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical_info',
            name='perc_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='perc_12',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='perc_ug',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='pg_perc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='teach_work_exp',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='tot_work_exp',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_10',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_12',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_phd',
            field=models.CharField(default='', max_length=100),
        ),
    ]