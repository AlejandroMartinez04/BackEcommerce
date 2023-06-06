from rest_framework import serializers
from .models import Client, Product

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('fullname', 'contact', 'email', 'password', 'admin')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'img', 'amount', 'category')