from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register(r'menu-items', MenuItemViewSet, basename='menuitem')
# urlpatterns = [
#     path('', include(router.urls)),  # This auto-generates all CRUD endpoints
# ]



urlpatterns = [
    path('menu-items/', MenuItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='menuitem-detail'),
]