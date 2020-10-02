from rest_framework import serializers
from restaurants.models import Restaurant, Deal, User, Order

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'deals', 'url')
        read_only_fields = ('deals',)

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        fields = ('id', 'title', 'description','original_price','new_price', 'restaurant', 'orders', 'url')
        read_only_fields = ('orders',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # orders = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=True, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'orders', 'url')
        read_only_fields = ('orders',)

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'deal', 'created', 'url')

