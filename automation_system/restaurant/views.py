from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer



def get_menu(request):
    user_systems = System.objects.filter(owner=request.user)
    menu_items = MenuItem.objects.filter(system__in=user_systems)
    return render(request, 'menu.html', {'menu_items': menu_items})

class MenuItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = MenuItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(menu_item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
            menu_item.delete()
            return Response({"message": "MenuItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except MenuItem.DoesNotExist:
            return Response({"error": "MenuItem not found."}, status=status.HTTP_404_NOT_FOUND)