from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ClientSerializer, ProductSerializer
from .models import Client, Product

class APIRootView(APIView):
    def get(self, request):
        data = {
            'message': 'Api working'
        }
        return JsonResponse(data)

class ClientViewSet(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer


class ClientEmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'email'


class ClientLoginView(generics.GenericAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        contraseña_ingresada = request.data.get('password')
        usuario = Client.objects.get(email=request.data.get('email'))
        if usuario.check_password(contraseña_ingresada):
            serializer = self.serializer_class(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong password'}, status=status.HTTP_401_UNAUTHORIZED)


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

