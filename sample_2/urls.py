from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('post', views.PostViewSet)
# router를 이용하여 하나의 URL에 2개의 view 처리

urlpatterns = [
    path('', include(router.urls)),
]
