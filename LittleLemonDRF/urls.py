from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('menu-items', views.ListCreateMenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemView.as_view()),
    path('groups/manager/users', views.ListCreateManagersView.as_view()),
    path('groups/manager/users/<int:pk>', views.DestroyManagerView.as_view()),
    path('groups/delivery-crew/users',views.ListCreateDriversView.as_view()),
    path('groups/delivery-crew/users/<int:pk>',views.ListCreateDriversView.as_view()),
    path('cart/menu-items', views.ListCreateCartItemsView.as_view()),
    path('cart/menu-items/<int:pk>', views.DeleteCartItemView.as_view()),
    path('orders', views.ListCreateOrdersView.as_view()),
    path('orders/<int:pk>', views.GetUpdateDeleteOrderView.as_view()),
] 