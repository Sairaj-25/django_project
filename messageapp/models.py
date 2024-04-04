from django.db import models
from django.contrib.auth.models import User

# Import the Product model
#from .models import Product  # Adjust the import path based on your project structure

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=100)
     


class Product(models.Model):
    Cat=((1,'Fruits'),(2,'Vegetables'),(3,'Dairy Products'),(4,'Groceries'),(5,'All'))
    name=models.CharField(max_length=40,verbose_name="Product name")
    price=models.FloatField()
    unit_quantity=models.CharField(max_length=40,verbose_name="unit_quantity")
    pdetails=models.CharField(max_length=100 ,verbose_name="product_details")
    cat=models.IntegerField(verbose_name="category",choices=Cat)
    is_active=models.BooleanField(default=True,verbose_name="available")
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.PositiveIntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=100)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.PositiveIntegerField(default=1)

