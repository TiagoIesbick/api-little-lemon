from rest_framework import serializers
from .models import *
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def validate_title(self, value):
        return bleach.clean(value)
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 0.01},        
        }
        
    def validate_title(self, value):
        return bleach.clean(value)
    
    
class MenuNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title']


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    
    
class CartSerializer(serializers.ModelSerializer): 
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    unit_price = serializers.SerializerMethodField(method_name='calc_unit_price')
    price = serializers.SerializerMethodField(method_name='calc_price')    
    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {            
            'quantity': {'min_value': 1}           
        }                
        
    def calc_unit_price(self, item:Cart):        
        return item.menuitem.price
    
    def calc_price(self, item:Cart):
        return item.quantity * item.menuitem.price
    
    
class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = ['menuitem', 'quantity', 'unit_price', 'price']      
        

class OrderSerializer(serializers.ModelSerializer):    
    user = serializers.CharField(read_only=True)    
    order_items = OrderItemSerializer(many=True, read_only=True)    
    total = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'order_items']


class PartialOrderSerializer(serializers.ModelSerializer):    
    user = serializers.StringRelatedField()    
    order_items = OrderItemSerializer(many=True, read_only=True)
    delivery_crew = serializers.StringRelatedField()    
    total = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'order_items']
        