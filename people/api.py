from .models import Client, Product
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer, ProductSerializer
from rest_framework import status
from rest_framework.response import Response

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        search_query = self.request.query_params.get('search', None)  # Obtener el parámetro de búsqueda
        if search_query:
            # Filtrar por correo electrónico o ID del cliente
            queryset = queryset.filter(email=search_query)
        return queryset

         


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search', None)  # Obtener el parámetro de búsqueda

        if search_query:
            # Filtrar por name o ID del producto
            queryset = queryset.filter(name=search_query)
        
        return queryset
