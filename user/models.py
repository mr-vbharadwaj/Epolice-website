from django.db import models

class Citizen(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    aadhaar_card_no = models.IntegerField(unique=True)


class Complaints(models.Model):
    citizen_name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    description = models.TextField
    time_of_complaint = models.DateTimeField
    status = models.CharField(choices= ( ('registered', 'registered'), ("in progress", "in progress"), ("resolved", "resolved") ) , max_length = 255)