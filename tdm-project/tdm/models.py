from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Driver(models.Model):
    driver_name = models.CharField(blank=True)
    company_name = models.CharField(blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    phone_alt = PhoneNumberField(blank=True)
    mc = models.CharField(blank=True)
    dot = models.CharField(blank=True)
    w9 = models.FileField(blank=True)
    truck_number = models.IntegerField(blank=True)
    trailer = models.CharField(blank=True)

class Customer(models.Model):
    customer_name = models.CharField(blank=True)
    contact_name = models.CharField(blank=True)
    street = models.CharField(blank=True)
    street_two = models.CharField(blank=True)
    city = models.CharField(blank=True)
    state = models.CharField(blank=True)
    zipcode = models.IntegerField(blank=True)
    customer_type = models.CharField(blank=True)
    phone = PhoneNumberField(blank=True)
    phone_alt = PhoneNumberField(blank=True)
    tax_id = models.CharField(blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

class Load(models.Model):
    # Foreign keys
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    # Model Fields
    load_date = models.DateField(blank=True)
    pickup_time = models.DateTimeField(blank=True)
    delivery_time = models.DateTimeField(blank=True)
    status = models.CharField(blank=True)
    commodity = models.CharField(blank=True)
    weight = models.FloatField(blank=True)
    driver_rate = models.FloatField(blank=True)
    miles = models.FloatField(blank=True)
    tarp_fee = models.FloatField(blank=True)
    detention = models.FloatField(blank=True)
    additional = models.FloatField(blank=True)
    notes = models.TextField(blank=True)
    invoice = models.FileField(blank=True)
    driver_settlement = models.CharField(blank=True)


