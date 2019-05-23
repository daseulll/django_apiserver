from django.urls import include, path
from . import views

urlpatterns = [
    path('post', views.post_list),
    path('post/<int:pk>', views.post_detail),
]
