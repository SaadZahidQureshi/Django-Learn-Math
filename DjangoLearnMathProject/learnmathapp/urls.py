
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("forgotPassword/", views.forgotPassword, name="forgotPassword"),
    path('index/', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("emailVerify/", views.EmailVerify, name="emailVerify"),
    path ('profileSetting/', views.profileSetting, name='profileSetting'),
    path ('popupQuiz/', views.popupQuiz, name='popupQuiz'),
    path('question/', views.question, name='question'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),
    path('question_with_image/',views.question_with_image, name='question_with_image'), 
    path("question_wrong_answer/", views.question_wrong_answer, name="question_wrong_answer"),


    # admin urls
    path('admin_login/', views.admin_login, name='admin_login'),
]
