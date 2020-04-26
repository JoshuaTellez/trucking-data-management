from django.contrib import admin
from .models import Carrier, Driver, Customer, Load

# Register your models here.
admin.site.register(Carrier)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Load)
