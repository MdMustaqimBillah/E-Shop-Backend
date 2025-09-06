from Products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'product_image', 'price', 'stock', 'created_at', 'updated_at']
        
        read_only_fields = ['id', 'created_at', 'updated_at']