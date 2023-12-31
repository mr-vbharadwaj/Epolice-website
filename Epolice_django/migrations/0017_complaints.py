# Generated by Django 5.0 on 2024-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epolice_django', '0016_delete_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizen_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=254)),
                ('citizen_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_of_incident', models.DateField()),
                ('time_of_complaint', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('registered', 'registered'), ('in progress', 'in progress'), ('resolved', 'resolved')], max_length=255)),
            ],
        ),
    ]
