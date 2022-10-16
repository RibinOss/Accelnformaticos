from django.db import models

from django.contrib.auth.models import AbstractUser

#AbstractUser: Puedes usar más atributos (id, first_name, last_name ...)
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

#Proxy model
#Aumentar funcionalidades
class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return ['Ya funciono']

#Aumentar Atributos
#Relación de uno a uno
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()