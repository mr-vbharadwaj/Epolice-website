# Generated by Django 5.0 on 2024-01-04 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Epolice_django', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Citizen',
        ),
        migrations.DeleteModel(
            name='Complaints',
        ),
    ]