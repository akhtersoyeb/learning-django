from django.contrib import admin

from .models import Customer, Product, Cart, OrderPlaced


admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(OrderPlaced)