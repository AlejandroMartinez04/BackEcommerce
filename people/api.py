from .models import Client, Product
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer, ProductSerializer


class ClientViewSet(viewsets.ModelViewSet):
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



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


