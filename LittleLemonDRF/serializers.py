from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from .models import MenuItem, Category,Order,OrderItem,Cart

class MenuItemsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        default = 0
    )
    class Meta:
        model = MenuItem
        fields = ['title','price','featured','category']
        

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )
    class Meta:
        model = MenuItem
        fields = ['user','menuitem','quantity','unit_price','price']
        
    
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )
    delivery_crew = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )
    class Meta:
        model = MenuItem
        fields = ['user','delivery_crew','status','date']
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(
        queryset = Order.objects.all()
    )
    menuitem = serializers.PrimaryKeyRelatedField(
        queryset = MenuItem.objects.all()
    )
    class Meta:
        model = MenuItem
        fields = ['order','menuitem','quantity','unit_price','price']
        
class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class DriverOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']