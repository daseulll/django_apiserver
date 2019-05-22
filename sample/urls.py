from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)
# router는 viewset을 지정할 때에만 사용한다.

urlpatterns = [
    path('', include(router.urls)),
    # path('post/', views.PostList.as_view()),
]