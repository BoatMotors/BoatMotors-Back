import datetime

from django.db import models

# Create your models here.
from register.models import User


class Category(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField()
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz


class Sub_ctg(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    sub_ctg = models.ForeignKey(Sub_ctg, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField()
    view = models.IntegerField()
    like = models.IntegerField()
    dis_like = models.IntegerField()
    price = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name


class OTP(models.Model):
    key = models.CharField(max_length=1024, unique=True)
    email = models.CharField(max_length=128)
    is_expired = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)
    state = models.CharField(max_length=128)
    is_confirmed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        if self.tries >= 5:
            self.is_expired = True

        return super(OTP, self).save(*args, **kwargs)
