from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComicViewSet

router = DefaultRouter()
router.register(r'comics', ComicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
