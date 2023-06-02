from django.urls import path
from rest_framework import routers
# from .api import ClientViewSet, ProductViewSet, EmailViewSet
from .views import ClientEmailDetailView, ClientViewSet, ProductViewSet, ProductIdView

# router = routers.DefaultRouter()

# router.register(r'api/client', ClientViewSet, 'client')
# router.register(r'api/product', ProductViewSet, 'product')
# router.register(r'api/email/<str:email>/', ClientEmailDetailView, 'email')
# router.register(r'api/product/<str:id>/', ProductIdView, 'product id')

# urlpatterns = router.urls

# urlpatterns = [
#     path('api/client/', ClientViewSet.as_view()),
# ]

urlpatterns = [
    path(r'api/client/', ClientViewSet.as_view(), name='client'),
    path(r'api/product/', ProductViewSet.as_view(), name='product'),
    path(r'api/client/<str:email>/', ClientEmailDetailView.as_view(), name='email'),
    path(r'api/product/<str:id>/', ProductIdView.as_view(), name='id')
]