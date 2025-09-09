from django.db import models
from Authentication.models import User
from Cart.models import Cart
import uuid
# Create your models here.

class Order(models.Model):
    
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart_items = models.ManyToManyField(Cart, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    order_id = models.UUIDField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = f"OID-{uuid.uuid4().hex[10:]}"
        super().save(*args, **kwargs)