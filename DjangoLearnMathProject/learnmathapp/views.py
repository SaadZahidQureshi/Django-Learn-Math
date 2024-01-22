import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from adminDashboard.models import Category,Level,Question
from django.core.serializers import serialize


# Create your views here.

@login_required(login_url='login')
def user_dashboard(request):
    context={
    'categories': Category.objects.all()
    }
    return render (request, 'user/home.html',context)

@login_required(login_url='login')
def popupQuiz(request):
    return render(request, 'user/Popup-Quiz.html')

@login_required(login_url='login')
def category(request,pk):
    context={}
    level_id= request.GET.get('level',None)

    if level_id:
        try:
            level = Level.objects.get(id=level_id)
            questions = Question.objects.filter(question_level=level)
            context['question'] = questions[0]
            context['questionno'] = 1
            context['total_questions'] = len(questions)
            context['correct_option'] = questions[0].correct_answer
            
        except Level.DoesNotExist:
            # Handle the case when the requested level does not exist
            pass
    category = Category.objects.get(id=pk)
    levels = Level.objects.filter(level_category = category)
    context['levels']=levels
    context['category']= category
    return render(request, 'user/Question.html', context)

@login_required(login_url='login')
def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

@login_required(login_url='login')
def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')

