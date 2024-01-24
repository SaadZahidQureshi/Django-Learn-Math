from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from adminDashboard.models import Category,Level,Question,Answer
from customAuth import helpers
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
    context['category'] = Category.objects.get(id=pk)
    context['levels'] = Level.objects.filter(level_category=context['category'])
    next_qsid = request.GET.get('qsid', None)
    qs_index = request.GET.get('qs_no', None)

    user = request.user
    user_answer = Answer.objects.filter(user=user).order_by('-updated_at').first()
    if user_answer:
        print(user_answer)
        answer_question = Question.objects.get(id = user_answer.question.id)
        answer_question_level = Level.objects.get(id = answer_question.question_level.id)
        level_no = answer_question_level.id
        print('level no',level_no)
        print('----',answer_question_level)
    else:
        level_no = 1
    try:        
        if level_no:
            try:
                category_level = context['levels'].get(id=level_no)
            except ObjectDoesNotExist:
                raise Http404('This level does not exist')
            
            qs = Question.objects.filter(question_level=category_level)
            context['current_level'] = category_level
            context['level_no'] =level_no
            
            if qs.exists():
                if next_qsid:
                    context['question'] = Question.objects.get(id=next_qsid)
                    context['questionno'] = int(qs_index) + 1
                    context['total_questions'] = len(qs)
                else:
                    context['question'] = qs.first()
                    context['questionno'] = 1
                    context['total_questions'] = len(qs)
            else:
                messages.warning(request, 'This level has 0 questions')
        else:
            messages.warning(request, 'Level number not provided in the request')
    except Http404 as e:    
        messages.error(request, f'Error : {str(e)} :(')
    except Exception as e:
        messages.error(request, f'Error : {str(e)} :(')

    return render(request, 'user/Question-wrong-ans.html', context)


@login_required(login_url='login')
def question_with_image(request):
    return render (request, 'user/Question-with-image.html')

@login_required(login_url='login')
def question_wrong_answer(request):
    return render (request, 'user/Question-wrong-ans.html')


@login_required(login_url='login')
def answer(request):
    category = request.GET.get('category_id', None)
    level_no = request.GET.get('level', None)
    qsid = request.GET.get('qsid', None)
    selected_option = request.GET.get('selected_option', None)
    time = request.GET.get('time',None)

    current_qs = Question.objects.get(id=qsid)
    levels = Level.objects.filter(level_category = category)
    levels_list = list(levels)
    current_level = levels.get(level_no = level_no)
    current_level_index = levels_list.index(current_level)

    if qsid is not None:
        try:
            question = Question.objects.get(id=qsid)
            if question.correct_answer == selected_option:
                is_answered = Answer.objects.filter(question = question).exists()
                if is_answered:
                    answer_instance = Answer.objects.get(question = question)
                    answer_instance.number_of_attempts = answer_instance.number_of_attempts + 1
                    answer_instance.selected_option = selected_option
                    answer_instance.time_taken = time
                    answer_instance.save()
                else:
                    Answer.objects.create(user = request.user, question = current_qs, selected_option = selected_option, number_of_attempts = 0, time_taken = time)

                next_question = helpers.get_next_question(request, category, level_no, qsid)
                if next_question:
                    return HttpResponseRedirect(next_question)
                else:
                    messages.success(request, 'Congratulations! You have completed all questions in this level.')
                    if current_level_index < len(levels_list) - 1:
                        next_level_no = levels_list[current_level_index + 1].level_no
                        return HttpResponseRedirect(reverse('category', args=[category])+ f'?level={next_level_no}')
            else:
                is_answered = Answer.objects.filter(question = question).exists()
                if is_answered:
                    answer_instance = Answer.objects.get(question = question)
                    answer_instance.number_of_attempts = answer_instance.number_of_attempts + 1
                    answer_instance.selected_option = selected_option
                    answer_instance.time_taken = time
                    answer_instance.save()
                else:
                    Answer.objects.create(user = request.user, question = current_qs, selected_option = selected_option, number_of_attempts = 0, time_taken = time)
                messages.error(request, 'Incorrect answer. Try again.')

        except ObjectDoesNotExist:
            messages.error(request, 'Question not found')

    return HttpResponseRedirect(reverse('category', args=[category]) + f'?level={level_no}')
