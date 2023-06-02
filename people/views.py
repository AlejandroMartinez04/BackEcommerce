from rest_framework import generics, permissions
from .serializers import ClientSerializer, ProductSerializer
from .models import Client, Product
from django.contrib.auth.hashers import make_password

class ClientViewSet(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

    def create_user(request):
        password = request.data.get('password')
        hashed_password = make_password(password)
        user = Client.objects.create(email=request.data.get('email'), password=hashed_password)

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

