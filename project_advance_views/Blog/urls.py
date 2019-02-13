from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampilan_blog, name='blog'),
    path('input_post/', views.input_post, name='input_post'),
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
]