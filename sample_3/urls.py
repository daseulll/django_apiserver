from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
# router.urls로 url 목록을 얻을 수 있음
# 2개의 URL을 처리하는 뷰 함수를 만들어서 등록

urlpatterns = [
    path('', include(router.urls)), # /sample_3/post
]
