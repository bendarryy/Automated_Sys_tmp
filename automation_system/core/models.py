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
