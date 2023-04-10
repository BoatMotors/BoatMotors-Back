from django.contrib.auth.base_user import BaseUserManager
from django.db import models
# Create your models here.






class ManagerUser(BaseUserManager):
    def create_user(self, phone, password, is_active=True, is_superuser=False, is_staff=False, *args, **kwargs):
        user = self.model(phone=phone,
                          password=password,
                          is_active=is_active,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        user.set_password(password)
        return user.save()

    def create_superuser(self, phone, password, **kwargs):
        return self.create_user(phone, password, is_superuser=True, is_staff=True, **kwargs)



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







