# Generated by Django 4.0 on 2022-12-01 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='speciality',
        ),
    ]