from Payments.models import Payment_Billing
from rest_framework import serializers

class PaymentBillingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    order = serializers.ReadOnlyField(source='order.order_id')
    
    class Meta:
        model = Payment_Billing
        fields = '__all__'
        read_only_fields = ['id', 'paid_at', 'created_at']