from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register("rooms?", views.RoomViewSet, basename='rooms')
router.register("dandcs?", views.DebtsClaimsViewSet, basename='dandcs')
router.register("accounts?", views.AccountViewSet, basename='accounts')
router.register("transactions?", views.TransactionViewSet, basename='transactions')
router.register("messages?", views.MessageViewSet, basename='messages') #Dorobiť message

urlpatterns = router.urls