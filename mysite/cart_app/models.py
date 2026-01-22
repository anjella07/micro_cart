from django.db import models


class Cart(models.Model):
    user_id = models.PositiveIntegerField()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)