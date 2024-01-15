
from django.urls import path
from . import views

urlpatterns = [
    path ('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path ('popupQuiz/', views.popupQuiz, name='popupQuiz'),
    path('question/<pk>', views.question, name='question'),
    path('question_with_image/',views.question_with_image, name='question_with_image'), 
    path("question_wrong_answer/", views.question_wrong_answer, name="question_wrong_answer"),


    # admin urls
    # path('admin_login/', views.admin_login, name='admin_login'),
]
