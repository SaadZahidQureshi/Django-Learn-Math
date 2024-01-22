from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.db.models import Q, Sum
from django.urls import reverse
from customAuth.models import User
from adminDashboard.models import CATEGORY_LIST, Category, Level, Question
from adminDashboard.forms import CategoryForm, LevelForm, QuestionForm


# Create your views here.

# Admin views here
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None and user.is_staff:
                login(request, user)
                return redirect('dashboard')  # Redirect to your desired URL after successful login
            else:
                messages.error(request, 'You not authorised.')
        print(form.errors)
        return render(request, 'admin_dashboard/login.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'admin_dashboard/login.html', {'form': form})

@login_required(login_url='admin-login')
def admin_logout(request):
    logout(request)
    return redirect('admin-login')

@login_required(login_url='admin-login')
def dashboard(request):
    context={
        'categories' : Category.objects.all().count(),
        'users' : User.objects.all().count(),
        'questions': Level.objects.aggregate(total_questions=Sum('number_of_questions'))
    }
    return render (request, 'admin_dashboard/dashboard.html',context)

@login_required(login_url='admin-login')
def profile(request):
    context={
        'form':PasswordChangeForm(request.user)
    }
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        print(form.errors)
    return render( request, 'admin_dashboard/profile.html',context)


# users views here 
@login_required(login_url='admin-login')
def users(request):

    search = request.GET.get('search-bar', None)
    start_date = request.GET.get('startdate', None)
    end_date = request.GET.get('enddate', None)
    context={
        'seachbar': search,
        'startdate': start_date,
        'enddate': end_date
    }

    records = User.objects.all()
    if start_date and end_date:
        records = records.filter(date_joined__range=(start_date, end_date))
    elif start_date:
        records = records.filter(date_joined__gte=start_date)
    elif end_date:
        records = records.filter(date_joined__lte=end_date)

    # Filter based on name
    if search:
        records = records.filter(Q(name__icontains=search) | Q(email__icontains=search))

    # Pagination
    paginator = Paginator(records, 4)
    page = request.GET.get('page')

    try:
        records_within_range = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        records_within_range = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        records_within_range = paginator.page(paginator.num_pages)


    # users = User.objects.all()
    users_count = records.count()
    context['users']= records_within_range
    context['users_count'] = users_count

    return render(request, 'admin_dashboard/users.html', context)

@login_required(login_url='admin-login')
def usersDetails(request, pk):
    user = User.objects.get(id=pk)
    return render (request, 'admin_dashboard/user-details.html',{'user':user})

@login_required(login_url='admin-login')
def usersDelete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users')


# category views here
@login_required(login_url='admin-login')
def categories(request):
    search = request.GET.get('search-bar', '')
    start_date = request.GET.get('startdate', '')
    end_date = request.GET.get('enddate', '')
    context={
        'seachbar': search,
        'startdate': start_date,
        'enddate': end_date,
        'category': request.GET.get('category',None)
    }

    records = Category.objects.all()

    if start_date and end_date:
        records = records.filter(created_at__range=(start_date, end_date))
    elif start_date:
        records = records.filter(created_at__gte=start_date)
    elif end_date:
        records = records.filter(created_at__lte=end_date)

    # Filter based on name
    if search:
        records = records.filter(Q(category_title__icontains=search) | Q(category_description__icontains=search))

    paginator = Paginator(records,4)
    page = request.GET.get('page')

    try:
        records_within_range = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        records_within_range = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        records_within_range = paginator.page(paginator.num_pages)

    category_count = records.count()
    context['categories']= records_within_range
    context['category_count'] = category_count

    return render(request, 'admin_dashboard/category.html', context)

@login_required(login_url='admin-login')
def addCategory(request):  
    context = {
        'form': CategoryForm(),
        'categories': CATEGORY_LIST.choices()
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        context['form']=form
        if form.is_valid():
            category = form.cleaned_data['category_title']
            form.save()
            return redirect(reverse('categories')+f'?addAlert=true&category={category}')
        print(form.errors)
    return render(request, 'admin_dashboard/add-category.html', context)

@login_required(login_url='admin-login')
def viewCategory(request,pk):
    category = Category.objects.get(id=pk)
    return render(request, 'admin_dashboard/view-category.html',{'category': category})

@login_required(login_url='admin-login')
def updateCategory(request,pk):
    category = Category.objects.get(id=pk)
    context={
        'form': CategoryForm(instance=category),
        'category':Category.objects.get(id=pk),
        'categories': Category.objects.all()
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES,instance=category)
        context['form']= form
        if form.is_valid():
            form.save()
            return redirect(reverse('categories')+f'?updateAlert=true&category={category.category_title}')
    return render(request, 'admin_dashboard/update-category.html',context)

@login_required(login_url='admin-login')
def deleteCategory(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories')


# level view here 
@login_required(login_url='admin-login')
def levels(request):
    context={
        'startdate': request.GET.get('startdate',None),
        'enddate': request.GET.get('enddate',None),
        'seachbar': request.GET.get('search-bar',None),
        'records' : Level.objects.all(),
        'records_count' : Level.objects.all().count,
        'levelno': request.GET.get('levelno',None)
    }

    if context['startdate'] and context['enddate']:
        context['records'] = context['records'].filter(created_at__range=(context['startdate'], context['enddate']))
    elif context['startdate']:
        context['records'] = context['records'].filter(created_at__gte=context['startdate'])
    elif context['enddate']:
        context['records'] = context['records'].filter(created_at__lte=context['enddate'])

    # Filter based on name
    if context['seachbar']:
        context['records'] = context['records'].filter(Q(level_no__icontains=context['seachbar']) | Q(number_of_questions__icontains=context['seachbar']))

    paginator = Paginator(context['records'],4)
    page = request.GET.get('page')

    try:
        records_within_range = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        records_within_range = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        records_within_range = paginator.page(paginator.num_pages)

    level_count = context['records'].count()
    context['records']= records_within_range
    context['level_count'] = level_count

    
    return render(request,'admin_dashboard/level.html' ,context)

@login_required(login_url='admin-login')
def addLevel(request):
    context={
        'categories': Category.objects.all(),
        'form': LevelForm()
    }
    if request.method =='POST':
        form = LevelForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success = (request, True)
            return redirect(reverse('levels')+f'?addlevelAlert=true')
        print(form.errors)
    return render(request, 'admin_dashboard/add-level.html',context)

@login_required(login_url='admin-login')
def levelDetails(request,pk):
    context= {
        'record': Level.objects.get(id=pk)
    }
    return render (request, 'admin_dashboard/level-details.html',context)

@login_required(login_url='admin-login')
def levelUpdate(request,pk):
    level = Level.objects.get(id=pk)
    context= {
        'record': level,
        'categories': Category.objects.all(),
        'form' : LevelForm(instance=level),
       
    }
    if request.method == 'POST':
        form = LevelForm(request.POST,instance=level)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect(reverse('levels')+f'?updatelevelAlert=true&levelno={level.level_no}')

    return render(request, 'admin_dashboard/update-level.html',context)

@login_required(login_url='admin-login')
def deleteLevel(request,pk):
    record = Level.objects.get(id=pk)
    record.delete()
    return redirect('levels')


# question views here
@login_required(login_url='admin-login')
def Questions(request):
    context = {
        'categories': Category.objects.all(),
        'category': request.GET.get('category', None),
        'level': request.GET.get('level', None),
        'startdate': request.GET.get('startdate', None),
        'enddate': request.GET.get('enddate', None),
        'search': request.GET.get('search-bar', None)
    }

    selected_category_title = context['category']
    selected_level = context['level']

    if selected_category_title:
        try:
            selected_category = Category.objects.get(category_title=selected_category_title)
            levels = Level.objects.filter(level_category=selected_category)
            context['levels']= levels
            context['records'] = Question.objects.filter(question_level__in=levels)
        except Category.DoesNotExist:
            context['records'] = Question.objects.none()
    else:
        context['records'] = Question.objects.all()
    
    if selected_level:
        levels = Level.objects.get(id=selected_level)
        context['level']= levels.level_no
        context['records'] = Question.objects.filter(question_level = levels)

    if context['startdate'] and context['enddate']:
        context['records'] = context['records'].filter(created_at__range=(context['startdate'], context['enddate']))
    elif context['startdate']:
        context['records'] = context['records'].filter(created_at__gte=context['startdate'])
    elif context['enddate']:
        context['records'] = context['records'].filter(created_at__lte=context['enddate'])

    # Filter based on name
    if context['search']:
        context['records'] = context['records'].filter(
            Q(question_title__icontains=context['search']) | Q(question_description__icontains=context['search'])
        )

    context['record_count'] = context['records'].count()

    paginator = Paginator(context['records'],4)
    page = request.GET.get('page')

    try:
        records_within_range = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        records_within_range = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        records_within_range = paginator.page(paginator.num_pages)

    question_count = context['records'].count()
    context['records']= records_within_range
    context['record_count'] = question_count


    return render(request, 'admin_dashboard/question.html', context)

@login_required(login_url='admin-login')
def addQuestion(request):
    
    context={
        'levels':Level.objects.all(),
        'form': QuestionForm()
    }
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect(reverse('questions')+f'?questionAddedAlert=true')
    return render(request, 'admin_dashboard/add-question.html',context)

@login_required(login_url='admin-login')
def viewQuestion(request,pk):
    context={
        'record': Question.objects.get(id=pk),
    }
    return render(request, 'admin_dashboard/question-details.html',context)

@login_required(login_url='admin-login')
def updateQuestion(request, pk):
    context={
        'record': Question.objects.get(id=pk),
        'levels': Level.objects.all(),
        'form': QuestionForm(instance=Question.objects.get(id=pk))
    }
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=Question.objects.get(id=pk))
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect(reverse('questions')+f'?questionUpdateAlert=true')
    return render(request, 'admin_dashboard/update-question.html', context)

@login_required(login_url='admin-login')
def deleteQuestion(request,pk):
    record = Question.objects.get(id=pk)
    record.delete()
    return redirect('questions')


