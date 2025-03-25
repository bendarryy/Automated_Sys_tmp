from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'(?P<system_id>\d+)/menu-items', MenuItemViewSet, basename="menu-items")


urlpatterns = [
    path('', include(router.urls)),  
]

# urlpatterns = [
#     path('menu-items/', MenuItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='menuitem-list'),
#     path('menu-items/<int:pk>/', MenuItemViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='menuitem-detail'),
# ]