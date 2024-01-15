from django.shortcuts import render
from adminDashboard.models import Category,Level


# Create your views here.


def user_dashboard(request):
    context={
    'categories': Category.objects.all()
    }
    return render (request, 'user/home.html',context)

def popupQuiz(request):
    return render(request, 'user/Popup-Quiz.html')

def question(request,pk):
    category = Category.objects.get(id=pk)
    levels = Level.objects.filter(level_category = category)
    context={
        'levels': levels,
        'category': category
    }
    return render(request, 'user/Question.html', context)

def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')

