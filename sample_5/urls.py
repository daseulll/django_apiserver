from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sample_5'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]