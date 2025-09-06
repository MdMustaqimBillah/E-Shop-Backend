from Cart.models import Cart
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    product = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity', 'purchased', 'added_at']
        
        read_only_fields = ['id', 'added_at', 'purchased']