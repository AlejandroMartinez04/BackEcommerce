from rest_framework import generics, permissions
from .serializers import ClientSerializer, ProductSerializer
from .models import Client, Product
import bcrypt


class ClientViewSet(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        request.data['password'] = hashed_password.decode('utf-8')

        return super().create(request, *args, **kwargs)

class ClientEmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'email'

    def partial_update(self, request, *args, **kwargs):
        password = request.data.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        request.data['password'] = hashed_password.decode('utf-8')

        return super().partial_update(request, *args, **kwargs)

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

