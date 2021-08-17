# Generated by Django 3.2 on 2021-06-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0021_rename_phno_document_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical_info',
            name='perc_10',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='perc_12',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='perc_ug',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='pg_degree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='pg_perc',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='pg_spec',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='pg_uni',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='phd_uni',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='skill_set',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='teach_work_exp',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='tot_work_exp',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='ug_degree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='ug_spec',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='ug_uni',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_10',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_12',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='technical_info',
            name='year_phd',
            field=models.IntegerField(default=''),
        ),
    ]
