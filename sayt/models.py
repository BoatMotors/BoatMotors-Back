from django.db import models

# Create your models here.



class User(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(128)
    state = models.CharField(max_length=50)
    region = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    adres = models.CharField(max_length=128)
    status = models.BooleanField

    def __str__(self):
        return self.first_name


class ctg(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz



class sub_ctg(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz


class product(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    img = models.ImageField
    view = models.IntegerField()
    like = models.IntegerField()
    dis_like = models.IntegerField()
    price = models.CharField(max_length=128)

    def __str__(self):
        return self.name_uz



class basket(models.Model):
    quantity = models.IntegerField()
    ptice = models.CharField(max_length=256)







