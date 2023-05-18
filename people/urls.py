from rest_framework import routers
from .api import ClientViewSet, ProductViewSet, EmailViewSet

router = routers.DefaultRouter()

router.register('api/client', ClientViewSet, 'client')
router.register('api/email', EmailViewSet, 'email')
router.register('api/product', ProductViewSet, 'product')

urlpatterns = router.urls
