from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemsSerializer, OrderSerializer,CartSerializer,OrderItemSerializer, BasicUserSerializer, DriverOrderUpdateSerializer
from .permissions import IsManager
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttles import ManagerThrottle



class ListCreateMenuItemsView(generics.ListCreateAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
    def get_permissions(self):
        if self.request.method == "GET":
            return []
        return [IsAuthenticated(), IsManager()]
    
    
class MenuItemView(generics.RetrieveUpdateDestroyAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsManager()]
    
    
class ListCreateManagersView(generics.ListCreateAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset = Group.objects.get(name="manager").user_set.all()
    serializer_class = BasicUserSerializer
    def get_permissions(self):
        return [IsAuthenticated(), IsManager()]
    def create(self,request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            manager_group = Group.objects.get(name = 'manager')
            user.groups.add(manager_group)
            return Response({"status": "Manager Created from manager group."}, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DestroyManagerView(generics.DestroyAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset =Group.objects.get(name="manager").user_set.all()
    serializer_class = BasicUserSerializer
    def get_permissions(self):
        return [IsAuthenticated(), IsManager()]
    
    def get_object(self):
        user = get_object_or_404(self.queryset,pk = self.kwargs["pk"] )
        manager_group = Group.objects.get(name = 'manager')
        user.groups.remove(manager_group)
        return user
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        return Response({"status": "User removed from manager group."}, status=status.HTTP_200_OK)


class ListCreateDriversView(generics.ListCreateAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset = Group.objects.get(name="delivery_driver").user_set.all()
    serializer_class = BasicUserSerializer
    def get_permissions(self):
        return [IsAuthenticated(), IsManager()]
    def create(self,request, *args, **kwargs):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            manager_group = Group.objects.get(name = 'deliver_crew')
            user.groups.add(manager_group)
            return Response({"status": "Delivery dro Created from delivery driver group."}, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class DriverView(generics.DestroyAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    queryset = Group.objects.get(name="delivery_driver").user_set.all()
    serializer_class = BasicUserSerializer

    def get_permissions(self):
        return [IsAuthenticated(), IsManager()]
    def get_object(self):
        user = get_object_or_404(self.queryset,k = self.kwargs['pk'])
        delivery_group = Group.objects.get(name = 'deliver_driver')
        user.groups.remove(delivery_group)
        return user
    def destroy(self,request, *args, **kwargs):
        user = self.get_object()
        return Response({"status": "User removed from Delivery group."}, status=status.HTTP_200_OK)

    
    

class ListCreateCartItemsView(generics.ListCreateAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)
    def get_permissions(self):
        return [IsAuthenticated()]


class DeleteCartItemView(generics.DestroyAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)
    def get_permission(self):
        return [IsAuthenticated()]
    


    
class ListCreateOrdersView(generics.ListCreateAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    serializer_class = OrderSerializer
    def get_queryset(self):
        if self.request.user.groups.filter(name="manager").exists():
            return Order.objects.all()
        elif self.request.user.groups.filter(name="delivery_driver").exists():
            return Order.objects.filter(delivery_crew = self.request.user)
        return Order.objects.filter(user = self.request.user)
    def get_permission(self):
        return [IsAuthenticated()]
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order_id = response.data.get("id")
        cart_items = Cart.objects.filter(user=self.request.user).values('menuitem', 'quantity','unit_price','price')
        for item in cart_items:
            item["order"] = order_id
        serializer = OrderItemSerializer(data = cart_items, many = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        Cart.objects.filter(user=self.request.user).delete()
        return response

class GetUpdateDeleteOrderView(generics.RetrieveUpdateDestroyAPIView):
    def get_throttle(self):
        if self.request.user.groups.filter(name="manager").exists():
            throttle_classes = [UserRateThrottle,AnonRateThrottle,ManagerThrottle]
        else:
            throttle_classes = [UserRateThrottle,AnonRateThrottle]
    
    def get_serializer_class(self):
        if self.action == "partial_update" and self.request.user.groups.filter(name="delivery_driver").exists():
            return DriverOrderUpdateSerializer
        if self.request.user.groups.filter(name="delivery_driver").exists() or self.request.user.groups.filter(name="manager").exists():
            return OrderSerializer
        return OrderItemSerializer
    
    def get_queryset(self):
        if self.request.user.groups.filter(name="delivery_driver").exists():
            return Order.objects.filter(delivery_crew = self.request.user)
        elif self.request.user.groups.filter(name="manager").exists():
            return Order.objects.all()
        order_ids = Order.objects.filter(user=self.request.user).values_list('pk', flat=True)
        return OrderItem.objects.filter(order__in = order_ids)
    def get_permission(self):
        if self.action == "destroy" or self.action == "update":
            return [IsAuthenticated(),IsManager()]
        return [IsAuthenticated()]
    def destroy(self,request, *args, **kwargs):
        instance = self.get_object()
        order_id = instance.pk
        response = super.destroy(self,request, *args, **kwargs)
        OrderItem.objects.filter(order = order_id).delete()
        return response
