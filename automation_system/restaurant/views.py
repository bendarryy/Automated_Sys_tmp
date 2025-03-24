from django.shortcuts import render
from .models import *
# Create your views here.



def get_menu(request):
    user_systems = System.objects.filter(owner=request.user)
    menu_items = MenuItem.objects.filter(system__in=user_systems)
    return render(request, 'menu.html', {'menu_items': menu_items})
