from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    # path('chat/', views.chat_view, name='chat'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('groups/', views.groups, name='groups'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/update/<int:pk>/', views.group_update, name='group_update'),
    path('group/<int:group_id>/', views.group_chat, name='group_chat')

]
