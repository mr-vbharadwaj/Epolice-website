# Generated by Django 5.0 on 2024-01-04 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Epolice_django', '0003_complaints'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Citizen',
        ),
        migrations.DeleteModel(
            name='Complaints',
        ),
    ]
