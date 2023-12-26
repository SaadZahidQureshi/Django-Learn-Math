from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path("forgotPassword/", views.forgotPassword, name="forgotPassword"),
    # path('index/', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("emailVerify/", views.emailVerify, name="emailVerify"),
    path("codeVerify/", views.codeVerify, name="codeVerify"),
    path ('profileSetting/', views.profileSetting, name='profileSetting'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),

]
