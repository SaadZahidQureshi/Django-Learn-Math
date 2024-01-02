import json
from .forms import OTPForm, SecondOTPForm, UserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import JsonResponse
from customAuth.sendEmail import Email
from customAuth.models import User
from django.urls import reverse
from customAuth import helpers
import datetime
import random




# Create your views here.
def emailVerify(request):
    if (request.method == 'POST'):  
        form = OTPForm(request.POST)
        if form.is_valid():
            response= helpers.send_email_save_record(request)
            print(response)
            return redirect(reverse('codeVerify') + f'?email={response["email"]}'+ f"&timeout={response['timeout']}")
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    
def codeVerify(request):
    input_email = request.GET.get('email','')
    timeout = request.GET.get('timeout')
    token = request.GET.get('token', None)
    context = {'email': input_email, 'timeout':timeout}
    form = SecondOTPForm()
    if(request.method == 'POST'):
        form = SecondOTPForm(request.POST)
        context['form'] = form
        if form.is_valid():
            response = helpers.otp_verify(request)
            if response['status'] == 200:
                token = response["token"]
                content = response['content']
                return redirect(reverse('signup') + f'?email={content}'+f"&token={token}")
            context['message'] = response['message']

    return render(request, 'user/Code-verify.html', context=context)


def signup(request):
    input_email = request.GET.get('email','')
    token = request.GET.get('token', None)
    context ={
        'email': request.GET.get('email',''),
        'token': request.GET.get('token', None)
    }
    # print(request.GET)
    if (request.method == 'POST'):
        print('test-1')
        form = UserForm(request.POST)
        if form.is_valid():
            print('test-2')
            email = form.cleaned_data['email']
            name =form.cleaned_data['name']
            response = helpers.checkEmail(email)
            message = response['message']
            if response['status'] == 200:
                print('test-3')
                password = form.cleaned_data['password']
                user = User(email=email,name=name)
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                return render(request, 'user/Signup.html', {'form': form, 'email': input_email, 'message': message})
        else:
            return render(request, 'user/Signup.html', {'form': form, 'email': input_email, 'token': token})
    else:
        form = UserForm() 
    return render(request, 'user/Signup.html', {'form': form, 'email': input_email, 'token': token})


def resendOTP(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        email = data.get('email')
        expiration_timestamp = data.get('expiration_timestamp')

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to your home page or any other desired page
            else:
                message = 'User does not exist!'
                return render(request, 'user/Login.html', {'form': form, 'message': message})
        else:
            message = 'Form Validations faild!'
            return render(request, 'user/Login.html', {'form': form, 'message': message})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/Login.html', {'form': form})

def forgotPassword(request):
    pass

def index(request):
    return render(request, 'user/Home.html')


def profileSetting(request):
    return render(request, 'user/Profile-setting.html')