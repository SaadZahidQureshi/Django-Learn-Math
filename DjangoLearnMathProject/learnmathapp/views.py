from django.shortcuts import render


# Create your views here.


def index(request):
    return render (request, 'user/home.html')

def popupQuiz(request):
    return render(request, 'user/Popup-Quiz.html')

def question(request):
    return render(request, 'user/Question.html')

def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')

# admin pages below here
def admin_login(request):
    return render(request, 'admin/login.html')