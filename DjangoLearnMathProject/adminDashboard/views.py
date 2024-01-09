from django.shortcuts import render,redirect
from customAuth.models import User
from customAuth.forms import CustomAuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
    users = User.objects.all()
    users_count = User.objects.all().count()
    return render(request, 'admin_dashboard/users.html', {'users':users, 'users_count':users_count})

@login_required(login_url='login')
def usersDetails(request, pk):
    user = User.objects.get(id=pk)
    return render (request, 'admin_dashboard/user-details.html',{'user':user})

@login_required(login_url='login')
def usersDelete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users')


