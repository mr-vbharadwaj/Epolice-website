from django.db import models

# Create your models here.

class Citizen(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    aadhaar_card_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.email)


class Complaints(models.Model):
    citizen_name = models.CharField(max_length = 255)
    user_email = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    citizen_email = models.EmailField()
    subject = models.CharField(max_length = 255)
    description = models.TextField()
    time_of_incident = models.DateField()
    time_of_complaint = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices= ( ('registered', 'registered'), ("in progress", "in progress"), ("resolved", "resolved") ) , max_length = 255)

    def __str__(self):
        return str(self.user_email)