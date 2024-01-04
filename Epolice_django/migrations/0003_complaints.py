# Generated by Django 5.0 on 2024-01-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epolice_django', '0002_delete_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizen_name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('time_of_complaint', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('registered', 'registered'), ('in progress', 'in progress'), ('resolved', 'resolved')], max_length=255)),
            ],
        ),
    ]
