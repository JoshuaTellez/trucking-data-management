# imports
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField


class Carrier(models.Model):
    company_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    phone_alt = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)
    street = models.CharField(max_length=64, blank=True, null=True)
    street_two = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    zipcode = USZipCodeField(blank=True, null=True)
    mc = models.CharField(max_length=64, blank=True, null=True)
    dot = models.CharField(max_length=64, blank=True, null=True)
    w9 = models.FileField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Driver(models.Model):
    # Foreign keys
    Carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, blank=True, null=True)

    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    phone_alt = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)
    mc = models.CharField(max_length=64, blank=True, null=True)
    dot = models.CharField(max_length=64, blank=True, null=True)
    w9 = models.FileField(blank=True, null=True)
    truck_number = models.IntegerField(blank=True, null=True)
    TRAILER_TYPES = [
        ('DV', 'Dry Van'),
        ('FB', 'Flatbed'),
        ('RF', 'Reefer'),
        ('CT', 'Conestoga'),
        ('SD', 'StepDeck'),
        ('OT', 'Other'),
    ]
    trailer = models.CharField(max_length=64, choices=TRAILER_TYPES, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    contact_name = models.CharField(max_length=64, blank=True, null=True)
    street = models.CharField(max_length=64, blank=True, null=True)
    street_two = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    zipcode = USZipCodeField(blank=True, null=True)
    customer_type = models.CharField(max_length=64, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    phone_alt = PhoneNumberField(blank=True, null=True)
    tax_id = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.customer_name


class Load(models.Model):
    # Foreign keys
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, blank=True, null=True)

    # Model Fields
    load_date = models.DateField(blank=True, null=True)
    pickup_time = models.DateTimeField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    STATUS_OPTIONS = [
        ('IT', 'In transit'),
        ('OP', 'Open'),
        ('PU', 'Picked up'),
        ('DL', 'Delivered'),
        ('IV', 'Invoiced'),
        ('CL', 'Closed'),
        ('MS', 'Missing'),
    ]
    status = models.CharField(max_length=64, choices=STATUS_OPTIONS, blank=True, null=True)
    commodity = models.CharField(max_length=64, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    driver_rate = models.FloatField(blank=True, null=True)
    miles = models.FloatField(blank=True, null=True)
    tarp_fee = models.FloatField(blank=True, null=True)
    detention = models.FloatField(blank=True, null=True)
    additional = models.FloatField(blank=True, null=True)
    rate_confirmation = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    invoice = models.FileField(blank=True, null=True)

    # Pickup Address
    pickup_street = models.CharField(max_length=64, blank=True, null=True)
    pickup_street_two = models.CharField(max_length=64, blank=True, null=True)
    pickup_city = models.CharField(max_length=64, blank=True, null=True)
    pickup_state = USStateField(blank=True, null=True)
    pickup_zipcode = USZipCodeField(blank=True, null=True)

    # Delivery Address
    delivery_street = models.CharField(max_length=64, blank=True, null=True)
    delivery_street_two = models.CharField(max_length=64, blank=True, null=True)
    delivery_city = models.CharField(max_length=64, blank=True, null=True)
    delivery_state = USStateField(blank=True, null=True)
    delivery_zipcode = USZipCodeField(blank=True, null=True)

    def __str__(self):
        return self.pk
