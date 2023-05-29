from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_regist'),
    path('registration/', views.register, name='register')
]