from users.models import CustomUser
from django.db import models

from store.models import Product


# Create your models here.
class StoreCart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, )
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    @property
    def amount(self):
        return self.quantity * self.product.price


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, )
    code = models.CharField(max_length=10, editable=False, )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=22, blank=True, )
    address = models.CharField(max_length=170, blank=True, )
    city = models.CharField(blank=True, max_length=30, )
    country = models.CharField(blank=True, max_length=30, )
    total = models.FloatField()
    status = models.CharField(max_length=10, default='New', choices=STATUS, )
    ip = models.CharField(blank=True, max_length=25, )
    admin_note = models.CharField(blank=True, max_length=150, )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=8, choices=STATUS, default='New', )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
