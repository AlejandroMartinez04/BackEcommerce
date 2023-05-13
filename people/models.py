from django.db import models

class People(models.Model):
    fullname = models.CharField(max_length=70)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Client(People):
    pass

class Manager(People):
    manager = models.BooleanField