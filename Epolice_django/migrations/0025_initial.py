# Generated by Django 5.0 on 2024-01-04 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Epolice_django', '0024_remove_complaints_user_email_delete_citizen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('aadhaar_card_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizen_name', models.CharField(max_length=255)),
                ('citizen_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_of_incident', models.DateField()),
                ('time_of_complaint', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('registered', 'registered'), ('in progress', 'in progress'), ('resolved', 'resolved')], max_length=255)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Epolice_django.citizen')),
            ],
        ),
    ]
