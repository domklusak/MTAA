from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register("rooms?", views.RoomViewSet, basename='rooms')
router.register("dandcs?", views.RoomViewSet, basename='dandcs')
router.register("users?", views.RoomViewSet, basename='users')
router.register("transactions?", views.RoomViewSet, basename='transactions')
router.register("messages?", views.RoomViewSet, basename='messages') #Dorobiť message

urlpatterns = router.urls