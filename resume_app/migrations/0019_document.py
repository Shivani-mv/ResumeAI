# Generated by Django 3.2 on 2021-06-10 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0018_auto_20210610_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.candidate_info')),
            ],
        ),
    ]
