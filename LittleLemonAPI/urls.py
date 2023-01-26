from django.urls import path
from .views import *

urlpatterns = [
    path('categories', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryView.as_view(), name='category'),
    path('menu-items', MenuItemsView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>', MenuItemView.as_view(), name='menu_item'),
    path('groups/manager/users', managers, name='managers'),
    path('groups/manager/users/<int:id>', remove_manager, name='remove_manager'),
    path('groups/delivery-crew/users', delivery_crew, name='delivery_crew'),
    path('groups/delivery-crew/users/<int:id>', remove_delivery_person, name='remove_delivery_person'),    
    path('cart/menu-items', CartView.as_view(), name='cart_view'),
    path('orders', OrdersView.as_view(), name='orders_view'),
    path('orders/<int:pk>', SingleOrderView.as_view(), name='single_order_view'),
]