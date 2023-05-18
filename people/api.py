from .models import Client, Product
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer, ProductSerializer
from rest_framework import generics
from django.db import connection


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


