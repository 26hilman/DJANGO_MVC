from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampilan_blog, name='blog')
]