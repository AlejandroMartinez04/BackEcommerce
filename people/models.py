from django.db import models

class People(models.Model):
    fullname = models.CharField(max_length=70)
    contact = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

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