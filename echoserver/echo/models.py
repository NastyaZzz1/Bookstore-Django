from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Books(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    author = models.CharField(max_length=80, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    genre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'books'


class Users(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.login
    
    class Meta:
        db_table = 'users'



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.product.cost * item.quantity for item in self.items.all())

    def __str__(self):
        if self.user:
            return f"Cart for user: {self.user.username}"
        else:
            return f"Cart (Session: {self.session_key})"
        
    class Meta:
        db_table = 'cart'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.cost * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart {self.cart.id}"
    
    class Meta:
        db_table = 'cart_item'