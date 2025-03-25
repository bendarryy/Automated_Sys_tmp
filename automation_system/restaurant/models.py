from django.db import models
from core.models import System , BaseMultiTenantModel
from django.contrib.auth.models import User

class MenuItem(BaseMultiTenantModel):
    """Menu for restaurants and cafes"""
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=[  
        ("food", "Food"),  
        ("drink", "Drink"),  
        ("dessert", "Dessert"),  
    ],  null=True)  # Categorize items
    image = models.ImageField(upload_to="images/menu_images/", blank=True, null=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Timestamp when added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when modified

    def __str__(self):
        return self.name
    # def __str__(self):
    #     return f"{self.name} - {self.price} {('✅' if self.is_available else '❌')}"

class Order(BaseMultiTenantModel):
    """Orders for restaurants and cafes"""
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)




class Staff(BaseMultiTenantModel):
    """Each system (restaurant) has its own staff"""
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('manager', 'Manager'), ('chef', 'Chef'), ('waiter', 'Waiter')])
