from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import *
from .serializers import *
from .permissions import *

# Documents used as consultation during development:
# https://www.cdrf.co/3.1/rest_framework.generics/RetrieveUpdateDestroyAPIView.html
# https://www.django-rest-framework.org/api-guide/relations/#inspecting-relationships 
# https://stackoverflow.com/questions/22250352/programmatically-create-a-django-group-with-permissions  


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):        
        if(self.request.method=='GET'):
            return []
        return [IsManagerOrSuperUser()]
    
    
class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):        
        if(self.request.method=='GET'):
            return []
        return [IsManagerOrSuperUser()]
    
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ['title', 'category__title']
    
    def get_permissions(self):        
        if(self.request.method=='GET'):
            return []
        return [IsManagerOrSuperUser()]
    
    
class MenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):        
        if(self.request.method=='GET'):
            return []
        return [IsManagerOrSuperUser()]


@api_view(['GET','POST'])
@permission_classes([IsManagerOrSuperUser])
def managers(request):    
    if request.method == 'GET':
        items = User.objects.filter(groups__name='Manager')
        serialized_items = UserSerializer(items, many=True)            
        return Response(serialized_items.data, status.HTTP_200_OK)    
    if 'username' in request.data:
        username = request.data['username']
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")        
        managers.user_set.add(user)        
        return Response({"message": f'{user.username} added to manager group'}, status.HTTP_201_CREATED)
    return Response({"message": "provide a valid username"}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsManagerOrSuperUser])
def remove_manager(request, id):  
    user = get_object_or_404(User, pk=id)    
    managers = Group.objects.get(name="Manager")
    managers.user_set.remove(user)
    return Response({"message": f'{user.username} removed from manager group'}, status.HTTP_200_OK)   
    

@api_view(['GET','POST'])
@permission_classes([IsManagerOrSuperUser])
def delivery_crew(request):
    if request.method == 'GET':
        items = User.objects.filter(groups__name='Delivery crew')
        serialized_items = UserSerializer(items, many=True)            
        return Response(serialized_items.data, status.HTTP_200_OK)    
    if 'username' in request.data:
        username = request.data['username']
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Delivery crew")        
        managers.user_set.add(user)        
        return Response({"message": f'{user.username} added to delivery crew'}, status.HTTP_201_CREATED)
    return Response({"message": "provide a valid username"}, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsManagerOrSuperUser])
def remove_delivery_person(request, id):  
    user = get_object_or_404(User, pk=id)    
    managers = Group.objects.get(name="Delivery crew")
    managers.user_set.remove(user)
    return Response({"message": f'{user.username} removed from delivery crew'}, status.HTTP_200_OK) 


class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.select_related('user', 'menuitem').all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)
    
    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response({"message": "Cart deleted"}, status.HTTP_204_NO_CONTENT)  
   

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.select_related('user', 'delivery_crew').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 
    filterset_fields = ['status', 'date', 'id']
    search_fields = ['order_items__menuitem__title', 'user__username', 'delivery_crew__username']  
    
    def list(self, request, *args, **kwargs):
        user = self.request.user
        if is_manager_or_superuser(user):
            queryset = self.get_queryset()          
        elif is_delivery_crew(user):
            # returns orders assigned to this delivery person, as well as orders placed by the same
            queryset = Order.objects.select_related('user', 'delivery_crew').filter(Q(delivery_crew=user) | Q(user=user))
        else:
            queryset = Order.objects.select_related('user', 'delivery_crew').filter(user=user)
        # because I overrode the list method it was necessary to adjust the filters and pagination
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)  
       
    def create(self, request, *args, **kwargs): 
        user = self.request.user
        cart = Cart.objects.filter(user=user)        
        if cart:
            order = Order.objects.create(user=user, total=0)
            serializer = CartSerializer(cart, many=True) 
            total = 0
            for item in serializer.data:
                OrderItem.objects.create(
                    order=order,
                    menuitem_id=item['menuitem'],
                    quantity=item['quantity'],
                    unit_price=item['unit_price'],
                    price=item['price']
                )
                total += item['price']
            order.total = total
            order.save()
            cart.delete()
            serializer_order = self.get_serializer(order)     
            return Response(serializer_order.data, status.HTTP_201_CREATED)
        return Response({"message": "The cart is empty."}, status.HTTP_400_BAD_REQUEST)


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.select_related('user', 'delivery_crew').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        if user != instance.user:
            if is_manager_or_superuser(user) or (is_delivery_crew(user) and user == instance.delivery_crew):
                instance = instance
            else:
                return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)   
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        user = request.user      
        if is_manager_or_superuser(user):
            delivery_crew_list = User.objects.filter(groups__name='Delivery crew').values_list('id', flat=True)
            try:  
                if int(request.data['delivery_crew']) in list(delivery_crew_list):          
                    return super().update(request, *args, **kwargs)
                return Response({"message": "The user assigned to the delivery don't belong to the delivery crew"}, status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": str(e)}, status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)     
         
    def destroy(self, request, *args, **kwargs):
        user = request.user
        if is_manager_or_superuser(user):
            return super().destroy(request, *args, **kwargs)
        return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        partial = kwargs.pop('partial', False)                     
        user = request.user
        instance = self.get_object()
        if is_delivery_crew(user) and user == instance.delivery_crew:
            serializer = PartialOrderSerializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"detail": "You do not have permission to perform this action."}, status.HTTP_403_FORBIDDEN)        
                 