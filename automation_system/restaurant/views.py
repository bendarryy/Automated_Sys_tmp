from django.forms import ValidationError
from django.shortcuts import render , get_object_or_404
from .models import *
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter menu items based on the requested system_id and optional category."""
        system_id = self.kwargs.get("system_id")  
        user = self.request.user 

        system = get_object_or_404(System, id=system_id, owner=user)
        
        queryset = MenuItem.objects.filter(system=system)

        category = self.request.query_params.get("category")

        if category:
            if category in MenuItemSerializer.VALID_CATEGORIES:
                queryset = queryset.filter(category=category)

        return queryset 
    
    def get_serializer_context(self):
        """Pass additional context to the serializer."""
        context = super().get_serializer_context()  # Get the default context
        context["view"] = self  # Optionally make the view accessible in the serializer
        return context
