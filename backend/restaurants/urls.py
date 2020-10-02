from django.urls import path, include
from rest_framework import routers
from . import views

router  = routers.DefaultRouter()
router.register('restaurants', views.RestaurantView)
router.register('deals', views.DealView)
router.register('users', views.UserView)
router.register('orders', views.OrderView)

urlpatterns = [
    path('', include(router.urls))
]
