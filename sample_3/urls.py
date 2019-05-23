from django.urls import include, path
from . import views

urlpatterns = [
    path('post', views.post_list),
]
