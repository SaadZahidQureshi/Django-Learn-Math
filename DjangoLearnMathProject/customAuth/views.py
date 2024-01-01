<<<<<<< HEAD
=======
from django.contrib.auth.forms import AuthenticationForm
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
from .forms import OTPForm, SecondOTPForm, UserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from customAuth.sendEmail import Email
<<<<<<< HEAD
from customAuth.models import User
=======
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
from django.urls import reverse
from customAuth import helpers
import datetime
import random




# Create your views here.
def emailVerify(request):
    if (request.method == 'POST'):  
        form = OTPForm(request.POST)
        if form.is_valid():
            input_email = form.cleaned_data['content']
            generated_otp = ''.join(random.choice('0123456789') for i in range(4))
            token = helpers.get_otp_verified_token(generated_otp,input_email)
<<<<<<< HEAD
            timeout =  datetime.datetime.now() + datetime.timedelta(minutes=5)
            Email.send(generated_otp,input_email)
            form.save(code=generated_otp, verification_token=token, timeout = timeout)
=======
            timeout =  datetime.datetime.now() + datetime.timedelta(minutes=99)
            Email.send(generated_otp,input_email)
            form.save(email=input_email, generated_otp=generated_otp, token=token, timeout = timeout)
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
            return redirect(reverse('codeVerify') + f'?email={input_email}')
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    
def codeVerify(request):
    input_email = request.GET.get('email','')
<<<<<<< HEAD
    context = {'email': input_email}

    form = SecondOTPForm()

    if(request.method == 'POST'):
        form = SecondOTPForm(request.POST)
        context['form'] = form
=======
    if(request.method == 'POST'):
        form = SecondOTPForm(request.POST)
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
        if form.is_valid():
            code = form.cleaned_data['code']
            content = form.cleaned_data['content']
            response = helpers.otp_verify(code, content)
    
            if response['status'] == 200:
                # token = response["token"]
                # &access_token={token}
                return redirect(reverse('signup') + f'?email={content}')
<<<<<<< HEAD
            context['message'] = response['message']

    return render(request, 'user/Code-verify.html', context=context)
=======
            else:
                return render(request, 'user/Code-verify.html', {'form': form,'email':input_email,'message':response['message']})
        else:
            return render(request, 'user/Code-verify.html', {'form': form,'email':input_email})
    else:
        form = SecondOTPForm()
    return render(request, 'user/Code-verify.html', {'form': form,'email':input_email})
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44


def signup(request):
    input_email = request.GET.get('email','')
    # input_email = request.GET.get('access_token','')
    if (request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            email = form.cleaned_data['email']
            name =form.cleaned_data['name']
            response = helpers.checkEmail(email)
            message = response['message']
            if response['status'] == 200:
                password = form.cleaned_data['password']
                user = User(email=email,name=name)
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                return render(request, 'user/Signup.html', {'form': form, 'email': input_email, 'message': message})
=======
            form.save()
            return redirect('login')
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
        else:
            return render(request, 'user/Signup.html', {'form': form, 'email': input_email})
    else:
        form = UserForm() 
    return render(request, 'user/Signup.html', {'form': form, 'email': input_email})


<<<<<<< HEAD

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
=======
# def login(request):

#     if(request.method == 'POST'):
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             is_exist = helpers.check_user(content, password)

#     return render(request, 'user/login.html')


def login(request):
    print("reached in login function")
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        print('test ...')
        if form.is_valid():
            print('clean data ',form.cleaned_data)
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to your home page or any other desired page
<<<<<<< HEAD
            else:
                message = 'User does not exist!'
                return render(request, 'user/Login.html', {'form': form, 'message': message})
        else:
            message = 'Form Validations faild!'
            return render(request, 'user/Login.html', {'form': form, 'message': message})
    else:
        form = CustomAuthenticationForm()
=======
    else:
        form = CustomAuthenticationForm()

>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
    return render(request, 'user/Login.html', {'form': form})

def forgotPassword(request):
    pass

def index(request):
<<<<<<< HEAD
    return render(request, 'user/Home.html')


def profileSetting(request):
    return render(request, 'user/Profile-setting.html')
=======
    return render(request, 'user/Home.html')
>>>>>>> a526412e62215d3a24d9cb5174500ca384eeba44
