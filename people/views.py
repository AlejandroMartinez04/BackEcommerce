from rest_framework import generics, permissions
from .serializers import ClientSerializer, ProductSerializer
from .models import Client, Product

class ClientViewSet(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class ClientEmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'email'

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search', None)  # Obtener el parámetro de búsqueda

        if search_query:
            queryset = queryset.filter(name=search_query)
        
        return queryset

class ProductIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

