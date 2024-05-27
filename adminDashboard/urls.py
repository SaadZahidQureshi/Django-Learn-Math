from django.urls import path
from . import views


urlpatterns = [
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # users urls here
    path('users/', views.users, name='users'),
    path('users/<pk>/', views.usersDetails, name='user-details'),
    path('user-delete/<pk>', views.usersDelete, name='user-delete'),
    path('profile/', views.profile, name='profile'),
    
    # category urls here
    path('categories/', views.categories, name='categories'),
    path('add-category/', views.addCategory, name='add-category'),
    path('view-category/<pk>/', views.viewCategory, name='view-category'),
    path('update-category/<pk>/', views.updateCategory, name='update-category'),
    path('delete-category/<pk>/', views.deleteCategory, name='delete-category'),

    # level urls here
    path('levels/', views.levels, name='levels'),
    path('level-details/<pk>', views.levelDetails, name='level-details'),
    path('level-update/<pk>', views.levelUpdate, name='level-update'),
    path('level-add/', views.addLevel, name='level-add'),
    path('level-delete/<pk>', views.deleteLevel, name='level-delete'),

    # question urls here
    path('questions/', views.Questions, name='questions'),
    path('add-question/', views.addQuestion, name='add-question'),
    path('view-question/<pk>/', views.viewQuestion, name='view-question'),
    path('update-question/<pk>/', views.updateQuestion, name='update-question'),
    path('delete-question/<pk>/', views.deleteQuestion, name='delete-question'),

]
