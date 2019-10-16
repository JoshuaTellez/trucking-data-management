from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Driver(models.Model):
    driver_name = models.CharField()
    company_name = models.CharField()
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    phone_alt = PhoneNumberField(blank=True)
    mc = models.CharField()
    DOT = models.CharField()
    w9 = models.FileField()
    truck_number = models.IntegerField()
    truck_type = models.CharField()

class Customer(models.Model):
    customer_name = models.CharField()
    street = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zipcode = models.IntegerField()
