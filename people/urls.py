from rest_framework import routers
from .api import ClientViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('api/client', ClientViewSet, 'client')
router.register('api/product', ProductViewSet, 'product')

urlpatterns = router.urls
