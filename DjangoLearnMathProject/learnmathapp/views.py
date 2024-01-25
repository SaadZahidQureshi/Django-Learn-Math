from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
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
    context={}
    category = Category.objects.get(id=pk)
    
    user = request.user
    user_last_answer = Answer.objects.filter(user = user).first()
    if user_last_answer:
        user_last_answer_question = Question.objects.get(id = user_last_answer.question.id)
        user_last_answer_question_level = Level.objects.filter(id = user_last_answer_question.question_level.id).first()
        user_last_answer_question_level_category = Category.objects.get(id=user_last_answer_question_level.level_category.id)
        all_levels_category = Level.objects.filter(level_category = user_last_answer_question_level_category)
        all_questions_current_level_count = Question.objects.filter(question_level = user_last_answer_question_level).count()
        all_questions_current_level = Question.objects.filter(question_level = user_last_answer_question_level)
        
        question_id = request.GET.get('question_id', None)
        if question_id:
            get_question = Question.objects.get(id = question_id)
            if(get_question.correct_answer == user_last_answer.selected_option):
                print('yes')
        context['category']=user_last_answer_question_level_category
        context['levels'] = all_levels_category
        context['current_level'] = user_last_answer_question_level
        context['total_questions'] = all_questions_current_level_count

        response = helpers.get_next_question(request, context['category'], context['current_level'].level_no, user_last_answer_question.id)
        print(response)

        try:
            if response:
                context['question'] = Question.objects.get(id = response['next_qs_id'])
                context['questionno'] = response['next_qs_index']
                context['current_level'] = response['level']
                context['category'] = response['category']
            else:
                messages.error(request, 'error ')

        except Exception as e:
            messages.warning(request, f'Error : {str(e)} :(')            

    else:
        local_level_no = 1
        local_level_no_questions_count = Question.objects.filter(question_level = local_level_no).count()
        local_level_no_questions = Question.objects.filter(question_level = local_level_no)
        local_level_no_questions = list(local_level_no_questions)

        context['category']=category
        context['levels'] = Level.objects.filter(level_category = category.id)
        context['current_level'] = context['levels'].get(level_no = local_level_no)
        context['total_questions'] = local_level_no_questions_count
        context['question'] =local_level_no_questions[0]
        context['questionno'] =local_level_no_questions.index(context['question'])+1


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
            if question.correct_answer == selected_option :
                is_answered = Answer.objects.filter(question = question, user = request.user).exists()
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
                    category = next_question['category']
                    level = next_question['level']
                    next_qs_id = next_question['next_qs_id']
                    next_qs_index = next_question['next_qs_index']
                    return HttpResponseRedirect(reverse('category', args=[next_question['category']])+ f'?level={category}&level={level}&next_qs_id={next_qs_id}&next_qs_index={next_qs_index}')                    # return redirect('category', next_question)
                else:
                    messages.success(request, 'Congratulations! You have completed all questions in this level.')
                    if current_level_index < len(levels_list) - 1:
                        next_level_no = levels_list[current_level_index + 1].level_no
                        return HttpResponseRedirect(reverse('category', args=[category])+ f'?level={next_level_no}')
            else:
                is_answered = Answer.objects.filter(question = question, user = request.user).exists()
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

    return HttpResponseRedirect(reverse('category', args=[category]) + f'?level={level_no}&question_id={question.id} ')
