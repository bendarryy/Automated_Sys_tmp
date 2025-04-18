from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BaseMultiTenantModel(models.Model):
    class Meta:
        abstract = True  # Ensure this class isn't created as a model

    @classmethod
    def for_user(cls, user):
        if user.is_superuser:
            return cls.objects.all()
        return cls.objects.filter(system__owner=user)

class System(models.Model):
    """Each generated system (e.g., a restaurant) is stored here"""
    SYSTEM_CATEGORIES = [
        ('restaurant', 'Restaurant'),
        ('cafe', 'Cafe'),
        ('supermarket', 'Supermarket'),
        ('workshop', 'Workshop'),
    ]
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=SYSTEM_CATEGORIES)

    def __str__(self):
        return f"{self.name} ({self.category})"

# Don't Touch  Under Devolpment 
class UserRole(models.Model):
    # Role types allowed for each system type
    ROLE_CHOICES = [
        # (value, label, [allowed_system_types])
        ('owner', 'Owner', ['restaurant', 'cafe', 'workshop']),
        ('manager', 'Manager', ['restaurant', 'cafe', 'workshop']),
        ('waiter', 'Waiter', ['restaurant']),  # Only for restaurants
        ('barista', 'Barista', ['cafe']),      # Only for cafes
        ('technician', 'Technician', ['workshop']),  # Only for workshops
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    
    class Meta:
        unique_together = ('user', 'system')  # One role per user per system

    def save(self, *args, **kwargs):
        # Validate role matches system type
        allowed_roles = [r for r in self.ROLE_CHOICES if self.system.system_type in r[2]]
        if self.role not in [r[0] for r in allowed_roles]:
            raise ValueError(f"Role '{self.role}' not allowed for {self.system.system_type} systems")
        super().save(*args, **kwargs)
        
  
# usage    fo UserRole 
        
# # This will work:
# restaurant = System.objects.get(system_type='restaurant')
# UserRole.objects.create(user=some_user, system=restaurant, role='waiter')

# # This will FAIL (raises ValueError):
# cafe = System.objects.get(system_type='cafe')
# UserRole.objects.create(user=some_user, system=cafe, role='waiter')  # Waiters can't be in cafes!