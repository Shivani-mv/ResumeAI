# Generated by Django 3.2 on 2021-06-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0010_auto_20210602_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='technical_info',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('perc_10', models.IntegerField()),
                ('year_10', models.IntegerField()),
                ('perc_12', models.IntegerField()),
                ('year_12', models.IntegerField()),
                ('ug_degree', models.CharField(max_length=100)),
                ('ug_uni', models.CharField(max_length=100)),
                ('ug_spec', models.CharField(max_length=100)),
                ('perc_ug', models.IntegerField()),
                ('pg_degree', models.CharField(max_length=100)),
                ('pg_uni', models.CharField(max_length=100)),
                ('pg_spec', models.CharField(max_length=100)),
                ('pg_perc', models.IntegerField()),
                ('phd_uni', models.CharField(max_length=100)),
                ('year_phd', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('tot_work_exp', models.IntegerField()),
                ('teach_work_exp', models.IntegerField()),
                ('skill_set', models.CharField(max_length=500)),
            ],
        ),
    ]
