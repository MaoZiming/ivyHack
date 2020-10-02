from django.shortcuts import render
from .models import Restaurant, User, Deal
from rest_framework import viewsets, permissions
from .serializers import RestaurantSerializer, UserSerializer, DealSerializer

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = RestaurantSerializer 

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class DealView(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer 