from django.contrib import admin

# Register your models here.
from .models import Driver, Customer, Load

admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Load)