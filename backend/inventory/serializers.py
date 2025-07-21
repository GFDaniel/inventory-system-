from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, InventoryMovement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']

class InventoryMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = InventoryMovement
        fields = ['id', 'product', 'product_name', 'movement_type', 'quantity', 
                 'description', 'user', 'user_name', 'created_at']
        read_only_fields = ['user']

    def validate(self, data):
        if data['movement_type'] == 'OUT':
            product = data['product']
            if data['quantity'] > product.stock:
                raise serializers.ValidationError(
                    "No se puede realizar una salida mayor al stock disponible"
                )
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
