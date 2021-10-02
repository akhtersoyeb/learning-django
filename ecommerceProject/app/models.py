from django.db import models

from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Assam', 'Assam'), 
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'), 
    ('West Bengal', 'West Bengal')
)

class Customer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    locality = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.IntegerField() 
    state = models.CharField(choices=STATE_CHOICES, max_length=150)

    def __str__(self): 
        return self.name

CATEGORY_CHOICES = (
    ('M', 'Mobile'), 
    ('L', 'Laptop'), 
    ('TW', 'Top Wear'), 
    ('BW', 'Bottor Wear')
)

class Product(models.Model): 
    title = models.CharField(max_length=150)
    selling_price = models.FloatField() 
    discounted_price = models.FloatField() 
    description = models.TextField() 
    brand = models.CharField(max_length=150)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to='productImg')

    def __str__(self): 
        return self.title 

class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self): 
        return str(self.id)

STATUS_CHOICES = (
    ('Pending', 'Pending'), 
    ('Packed', 'Packed'), 
    ('On The Way', 'On The Way'), 
    ('Delivered', 'Delivered'), 
    ('Cancel', 'Cancel'), 
)


class OrderPlaced(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, 
                                default='Pending') 


