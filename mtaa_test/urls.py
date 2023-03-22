from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register("rooms?", views.RoomViewSet, basename='rooms')

urlpatterns = router.urls