from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
    return render(request, 'user/login.html')

def forgotPassword(request):
    return render(request ,'user/Reset-Password.html')

def signup(request):
    return render(request, 'user/Signup.html')

def EmailVerify(request):
    return render(request, 'user/Email-verify.html')

def index(request):
    return render (request, 'user/home.html')

def profileSetting(request):
    return render(request, 'user/Profile-Setting.html')

def popupQuiz(request):
    return render(request, 'user/Popup-Quiz.html')

def question(request):
    return render(request, 'user/Question.html')
@csrf_exempt
def delete_profile_picture(request):
    default_image_url = '/static/user/assets/svg/profile1-blue.svg'
    print(default_image_url)
    return JsonResponse({'default_image_url': default_image_url})

def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')


# admin pages below here
def admin_login(request):
    return render(request, 'admin/login.html')