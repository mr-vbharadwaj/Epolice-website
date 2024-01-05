from django.db import models

# Create your models here.

class Officer(models.Model):
    officer_id = models.IntegerField(unique=True)
    officer_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    officer_mobile = models.IntegerField()
    officer_name = models.CharField(max_length=255)
    officer_station = models.CharField(max_length=255)

    def __str__(self):
        return self.officer_name + "\t  " + self.officer_station