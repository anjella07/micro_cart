from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'cart', CartViewSet)
router.register(r'cart_item', CartItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]