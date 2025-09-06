from Orders.models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    order = serializers.ReadOnlyField(source='order.cart_id')
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'ordered_at', 'created_at']