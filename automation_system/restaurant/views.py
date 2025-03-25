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

# class MenuItemViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = MenuItem.objects.all()
#         serializer = MenuItemSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = MenuItemSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         try:
#             menu_item = MenuItem.objects.get(pk=pk)
#         except MenuItem.DoesNotExist:
#             return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MenuItemSerializer(menu_item)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         try:
#             menu_item = MenuItem.objects.get(pk=pk)
#         except MenuItem.DoesNotExist:
#             return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MenuItemSerializer(menu_item, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         try:
#             menu_item = MenuItem.objects.get(pk=pk)
#         except MenuItem.DoesNotExist:
#             return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MenuItemSerializer(menu_item, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             menu_item = MenuItem.objects.get(pk=pk)
#             menu_item.delete()
#             return Response({"message": "MenuItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#         except MenuItem.DoesNotExist:
#             return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)