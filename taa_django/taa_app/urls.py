from django.urls import path 
from rest_framework.routers import DefaultRouter
from .views import current_user, UserList, HikeViewSet, BreweryViewSet

router = DefaultRouter()
router.register(r'hike', HikeViewSet, basename='hike')
router.register(r'brewery', BreweryViewSet, basename='brewery')

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()), 
]

urlpatterns += router.urls 