from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('login/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('users/<pk>/', views.usersDetails, name='user-details'),
    path('user-delete/<pk>', views.usersDelete, name='user-delete'),

    
    
    path('categories/', views.categories, name='categories'),
    path('add-category/', views.addCategory, name='add-category'),
    path('view-category/<pk>/', views.viewCategory, name='view-category'),
    path('update-category/<pk>/', views.updateCategory, name='update-category'),
    path('delete-category/<pk>/', views.deleteCategory, name='delete-category'),



]
