from django.contrib.auth.forms import AuthenticationForm
from customAuth.forms import CustomAuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.contrib import messages
from customAuth.models import User
from datetime import datetime
# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(email,password)
            user = authenticate(request, email=email, password=password)
            print(user.is_staff)
            
            if user is not None and user.is_staff:
                login(request, user)
                # messages.success(request, f'Welcome, {email}!')
                return redirect('dashboard')  # Redirect to your desired URL after successful login
            else:
                messages.error(request, 'You not authorised.')
        print(form.errors)
        return render(request, 'admin_dashboard/login.html', {'form': form})


    else:
        form = AuthenticationForm()

    return render(request, 'admin_dashboard/login.html', {'form': form})

@login_required(login_url='login')
def admin_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render (request, 'admin_dashboard/dashboard.html')

@login_required(login_url='login')
def users(request):

    search = request.GET.get('search-bar', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    context={
        'seachbar': search,
        'startdate': start_date,
        'enddate': end_date
    }

    # if start_date and end_date:
    #     records_within_range = User.objects.filter(date_joined__range=(start_date, end_date))
    # elif start_date:
    #     records_within_range = User.objects.filter(date_joined__gte=start_date)
    # elif end_date:
    #     records_within_range = User.objects.filter(date_joined__lte=end_date)
    # else:
    #     # Handle the case where neither start_date nor end_date is provided
    #     records_within_range = User.objects.all()

    # if search:
    #     records_within_range = records_within_range.filter(name__icontains=search)

    records = User.objects.all()
    if start_date and end_date:
        records = records.filter(date_joined__range=(start_date, end_date))
    elif start_date:
        records = records.filter(date_joined__gte=start_date)
    elif end_date:
        records = records.filter(date_joined__lte=end_date)

    # Filter based on name
    if search:
        records = records.filter(name__icontains=search)

    # Pagination
    paginator = Paginator(records, 3)
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
    # users_count = records.count()
    context['users']= records_within_range
    # context['users_count'] = users_count

    return render(request, 'admin_dashboard/users.html', context)

@login_required(login_url='login')
def usersDetails(request, pk):
    user = User.objects.get(id=pk)
    return render (request, 'admin_dashboard/user-details.html',{'user':user})

@login_required(login_url='login')
def usersDelete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users')

def usersFilter(request):
    print("im filtering...")

def categories(request):
    pass