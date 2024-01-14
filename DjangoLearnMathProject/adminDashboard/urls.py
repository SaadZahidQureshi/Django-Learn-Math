from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('login/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # users urls here
    path('users/', views.users, name='users'),
    path('users/<pk>/', views.usersDetails, name='user-details'),
    path('user-delete/<pk>', views.usersDelete, name='user-delete'),

    
    # category urls here
    path('categories/', views.categories, name='categories'),
    path('add-category/', views.addCategory, name='add-category'),
    path('view-category/<pk>/', views.viewCategory, name='view-category'),
    path('update-category/<pk>/', views.updateCategory, name='update-category'),
    path('delete-category/<pk>/', views.deleteCategory, name='delete-category'),


    # level urls here
    path('levels/', views.levels, name='levels'),
    path('level-details/', views.levelDetails, name='level-details'),
    path('level-update/', views.levelUpdate, name='level-update'),
    path('add-update/', views.addLevel, name='add-update'),



]
