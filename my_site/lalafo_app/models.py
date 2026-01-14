from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    price = models.PositiveSmallIntegerField()
    phone = PhoneNumberField()
    product_type = models.BooleanField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    owner = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} {self.price}'
