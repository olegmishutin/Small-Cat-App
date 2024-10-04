from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')

app_name = 'cats'
urlpatterns = [
    path('', include(router.urls))
]
