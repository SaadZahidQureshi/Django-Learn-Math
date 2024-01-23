import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from adminDashboard.models import Category,Level,Question,Answer

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
def category(request, pk):
    context = {}

    context['category'] = get_object_or_404(Category, id=pk)
    context['levels'] = Level.objects.filter(level_category=context['category'])

    try:
        level_no = request.GET.get('level', None)
        if level_no:
            try:
                category_level = context['levels'].get(level_no=level_no)
            except ObjectDoesNotExist:
                raise Http404('This level does not exist')

            qs = Question.objects.filter(question_level=category_level)
            context['current_level'] = category_level

            # Check if questions exist for the given level
            if qs.exists():
                context['question'] = qs.first()
                context['questionno'] = 1
                context['total_questions'] = len(qs)
            else:
                print('--> This level has 0 questions')
        else:
            # Handle the case where level_no is not provided
            print('Level number not provided in the request')

    except Http404 as e:
        # Handle 404 errors (category or level not found)
        print(str(e))

    except Exception as e:
        # Handle other unexpected errors
        print(f'An unexpected error occurred: {str(e)}')
    print('her at bottom ', context['question'].question_image)
    return render(request, 'user/Question-wrong-ans.html', context)

@login_required(login_url='login')
def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

@login_required(login_url='login')
def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')

@login_required(login_url='login')
def answer(request):
    context={}
    # Handle user's attempt
    category = request.GET.get('category_id',None)
    level_no = request.GET.get('level', None)
    qsid = request.GET.get('qsid', None)
    selected_option = request.GET.get('selected_option', None)

    if qsid is not None:
        try:
            question = get_object_or_404(Question, id=qsid)
            if question.correct_answer == selected_option:
                # Answer.objects.create(selected_option=selected_option, question=question, user=request.user, number_of_attempts=0)
                print('matched-success')
            else:
                print('Failure')
                # Answer.objects.create(selected_option=selected_option, question=question, user=request.user, number_of_attempts=0)
            print('Done')

        except ObjectDoesNotExist:
            print('Question not found')
    return HttpResponseRedirect('/learnmath/category/'+category+'?level='+level_no )