from django.contrib import admin
from .models import Product,Category,Order
from .models import Customer

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
