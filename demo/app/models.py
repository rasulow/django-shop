from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


        
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()    
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='images/')
    image4 = models.ImageField(null=True, blank=True, upload_to='images/')
    image5 = models.ImageField(null=True, blank=True, upload_to='images/')
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self) -> str:
        return self.name
        

class Order(models.Model):
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    note = models.TextField(null=True)
    status = models.BooleanField(null=False, default=False)
    
    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
    def __str__(self) -> str:
        return self.user.username