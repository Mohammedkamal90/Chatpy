from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='your_custom_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
