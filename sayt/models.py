from django.db import models

# Create your models here.

class Category(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz



class Sub_ctg(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField
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







