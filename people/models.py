from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class People(models.Model):
    fullname = models.CharField(max_length=70)
    contact = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    saldo = models.BigIntegerField()

    def save(self, *args, **kwargs):
        # Encripta la contraseña antes de guardarla
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Compara la contraseña encriptada con la contraseña ingresada
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.fullname
    class Meta:
        abstract = True


class Client(People):
    admin = models.CharField(max_length=5)



#products
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    img = models.CharField(max_length=300)
    amount = models.IntegerField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name