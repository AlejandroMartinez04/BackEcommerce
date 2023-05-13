from rest_framework import routers
from .api import ClientViewSet

router = routers.DefaultRouter()

router.register('api/client', ClientViewSet, 'client')

urlpatterns = router.urls
