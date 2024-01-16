
from django.urls import path
from . import views
from customAuth.views import profileSetting

urlpatterns = [
    path ('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path ('popupQuiz/', views.popupQuiz, name='popupQuiz'),
    path('category/<pk>', views.category, name='category'),
    path('question_with_image/',views.question_with_image, name='question_with_image'), 
    path("question_wrong_answer/", views.question_wrong_answer, name="question_wrong_answer"),
    path ('profile-Setting/', profileSetting, name='profileSetting'),


    # admin urls
    # path('admin_login/', views.admin_login, name='admin_login'),
]
