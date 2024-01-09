from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('index/', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("emailVerify/", views.emailVerify, name="emailVerify"),
    path("codeVerify/", views.codeVerify, name="codeVerify"),
    path ('profile-Setting/', views.profileSetting, name='profileSetting'),
    path('resendOTP/', views.resendOTP, name='resendOTP'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),
    path('reset-password/', views.resetPassword, name='resetPassword'),

]
