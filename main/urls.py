from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('cases', views.Cases.as_view(), name='cases'),
    path('blog', views.Blog.as_view(), name='blog'),
]