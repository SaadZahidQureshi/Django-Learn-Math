from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('login/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('users/<pk>/', views.usersDetails, name='user-details'),
    path('user-delete/<pk>', views.usersDelete, name='user-delete'),
    path('users/', views.usersFilter, name='user-filter'),
    
    
    path('categories/', views.categories, name='categories'),



]
