from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampilan_mentor, name='mentor')
]