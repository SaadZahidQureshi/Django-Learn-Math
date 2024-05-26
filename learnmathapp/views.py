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
    skip = request.GET.get('skip', False)
    correct = 0
    attempted = 0
    wrong = 0

    answers = Answer.objects.prefetch_related('question', 'question__question_level', 'question__question_level__level_category').filter(user=request.user, question__question_level__level_category_id=pk).order_by('-question__question_level__level_no')
    # print(answers.values())

    user_last_answer = answers.first()
    # print(user_last_answer.id)
    if user_last_answer:
        user_last_answer_question = user_last_answer.question
        user_last_answer_question_level = user_last_answer.question.question_level
        user_last_answer_question_level_category = user_last_answer.question.question_level.level_category
        all_levels_category = user_last_answer_question_level_category.levels.all()
        all_questions_current_level = user_last_answer_question_level.questions.all()
        all_questions_current_level_count = all_questions_current_level.count()
        
        if category == user_last_answer_question_level_category:
            
            context['category']=user_last_answer_question_level_category
            context['levels'] = all_levels_category
            context['current_level'] = user_last_answer_question_level
            context['total_questions'] = all_questions_current_level_count


            for question in all_questions_current_level:
                answer_of_question = Answer.objects.filter(question = question, user = request.user).first()
                if answer_of_question:
                    if question.correct_answer == answer_of_question.selected_option:
                        correct += 1
                        attempted += 1
                    else:
                        wrong += 1
                        attempted += 1
                
            context['correct'] = correct
            context['wrong'] = wrong
            context['attempted'] = attempted
            
            if user_last_answer.selected_option == user_last_answer_question.correct_answer or skip == 'True':
                question_response = helpers.get_next_question(request, context['category'], context['current_level'].level_no, user_last_answer_question.id)
                print(user_last_answer_question.id)
                try:
                    if question_response:
                        context['question'] = Question.objects.get(id = question_response['next_qs_id'])
                        context['questionno'] = question_response['next_qs_index'] + 1
                    else:
                        if (all_questions_current_level_count > 3 and correct >= 3) or (all_questions_current_level_count < 3 and correct == all_questions_current_level_count) :
                            level_response = helpers.get_next_level(request, context['category'], context['current_level'].level_no)

                            if level_response:
                                instance_new_level = Level.objects.get(id = level_response['next_level_id'])
                                questions_of_new_level = Question.objects.filter(question_level = instance_new_level)

                                context['question'] = questions_of_new_level.first()
                                context['questionno'] = 1
                                context['current_level'] = instance_new_level
                                context['total_questions'] = questions_of_new_level.count()

                                context['correct'] = 0
                                context['wrong'] = 0
                                context['attempted'] = 0
                                    
                                messages.success(request, 'Congratulations! You have completed all questions in this level.')
                            else:
                                messages.error(request, 'Error occured while loading next Level ')
                        else:
                            current_level = context['current_level']
                            questions  = Question.objects.filter(question_level = current_level)
                            context['question'] = questions.first()
                            context['questionno'] = 1

                            context['correct'] = 0
                            context['wrong'] = 0
                            context['attempted'] = 0
                            
                            messages.warning(request, 'You need to re-try this level')

                except Exception as e:
                    print({str(e)})
                    messages.warning(request, f'Error : {str(e)} :(')  

            else:
                all_questions_current_level = list(all_questions_current_level)
                index_of_last_question = all_questions_current_level.index(user_last_answer_question)
                context['question'] = user_last_answer_question
                context['questionno'] = index_of_last_question + 1

        else:           
            context['category']= category
            # response = helpers.get_current_level_category(request,category)

            context['levels'] = Level.objects.filter(level_category = category)
            context['current_level'] = context['levels'][0]
            questions = Question.objects.filter(question_level = context['levels'][0].id)

            if questions.exists():
                context['question']= questions.first()
                context['questionno'] = 1
                context['total_questions'] = questions.count()
                
                context['correct'] = 0
                context['wrong'] = 0
                context['attempted'] = 0
            else:
                messages.warning(request, 'this level have no questions yet.' )
    else:

        levels = Level.objects.filter(level_category = category.id).exists()
        if levels:
            all_levels = Level.objects.filter(level_category = category.id)
            local_level_no = all_levels.first().level_no
            local_level_no_questions_count = Question.objects.filter(question_level = all_levels.first().id).count()
            local_level_no_questions = Question.objects.filter(question_level = all_levels.first().id)
            local_level_no_questions = list(local_level_no_questions)

            if local_level_no_questions_count > 0:

                context['category']=category
                context['levels'] = all_levels
                context['current_level'] = context['levels'].get(level_no = local_level_no)
                context['total_questions'] = local_level_no_questions_count
                context['question'] =local_level_no_questions[0]
                context['questionno'] =local_level_no_questions.index(context['question'])+1

                context['correct'] = 0
                context['wrong'] = 0
                context['attempted'] = 0
            else:
                context['category']=category
                context['levels'] = all_levels
                messages.info(request, 'This category level has no questions yet')
        else:
            messages.info(request, 'This category has no levels yet')
            return redirect('user-dashboard')

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
                    answer_instance = Answer.objects.filter(question = question).first()
                    answer_instance.number_of_attempts = answer_instance.number_of_attempts + 1
                    answer_instance.selected_option = selected_option
                    answer_instance.time_taken = time
                    answer_instance.save()
                else:
                    Answer.objects.create(user = request.user, question = current_qs, selected_option = selected_option, number_of_attempts = 0, time_taken = time)
            else:
                is_answered = Answer.objects.filter(question = question, user = request.user).exists()
                if is_answered:
                    answer_instance = Answer.objects.filter(question = question).first()
                    answer_instance.number_of_attempts = answer_instance.number_of_attempts + 1
                    answer_instance.selected_option = selected_option
                    answer_instance.time_taken = time
                    answer_instance.save()
                else:
                    Answer.objects.create(user = request.user, question = current_qs, selected_option = selected_option, number_of_attempts = 0, time_taken = time)
                messages.error(request, 'Incorrect answer. Try again.')

        except ObjectDoesNotExist:
            messages.error(request, 'Question not found')

    return HttpResponseRedirect(reverse('category', args=[category]))
