# from .models import Client, Product
# from rest_framework import viewsets, permissions
# from .serializers import ClientSerializer, ProductSerializer


# class EmailViewSet(viewsets.ModelViewSet):
#     # queryset = Client.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ClientSerializer
#     lookup_field = 'email'

# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ClientSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ProductSerializer
#     lookup_field = 'id'