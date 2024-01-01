from .forms import OTPForm, SecondOTPForm, UserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
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
            input_email = form.cleaned_data['content']
            generated_otp = ''.join(random.choice('0123456789') for i in range(4))
            token = helpers.get_otp_verified_token(generated_otp,input_email)
            timeout =  datetime.datetime.now() + datetime.timedelta(minutes=5)
            Email.send(generated_otp,input_email)
            form.save(code=generated_otp, verification_token=token, timeout = timeout)
            return redirect(reverse('codeVerify') + f'?email={input_email}')
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    
def codeVerify(request):
    input_email = request.GET.get('email','')
    context = {'email': input_email}

    form = SecondOTPForm()

    if(request.method == 'POST'):
        form = SecondOTPForm(request.POST)
        context['form'] = form
        if form.is_valid():
            code = form.cleaned_data['code']
            content = form.cleaned_data['content']
            response = helpers.otp_verify(code, content)
    
            if response['status'] == 200:
                # token = response["token"]
                # &access_token={token}
                return redirect(reverse('signup') + f'?email={content}')
            context['message'] = response['message']

    return render(request, 'user/Code-verify.html', context=context)


def signup(request):
    input_email = request.GET.get('email','')
    # input_email = request.GET.get('access_token','')
    if (request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
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
        else:
            return render(request, 'user/Signup.html', {'form': form, 'email': input_email})
    else:
        form = UserForm() 
    return render(request, 'user/Signup.html', {'form': form, 'email': input_email})



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