import json
from .forms import OTPForm, SecondOTPForm, UserForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import JsonResponse
from customAuth.models import User
from django.urls import reverse
from customAuth import helpers




# Create your views here.
def emailVerify(request):
    if (request.method == 'POST'):  
        form = OTPForm(request.POST)
        if form.is_valid():
            response= helpers.send_email_save_record(request)
            request.session['veri1'] = True
            return redirect(reverse('codeVerify') + f'?email={response["email"]}')
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    

def codeVerify(request):
    key =  request.session.get('veri1',None)
    if key:
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
                    request.session.pop('veri1',None)
                    request.session['veri2'] = True
                    return redirect(reverse('signup') + f'?email={content}'+f"&token={token}")
                context['message'] = response['message']
        return render(request, 'user/Code-verify.html', context=context)
    return redirect('emailVerify')


def signup(request):
    key =request.session.get('veri2', None)
    if key:
        context ={
            'email': request.GET.get('email',''),
            'token': request.GET.get('token', None)
        }
        form = UserForm() 
        if (request.method == 'POST'):
            form = UserForm(request.POST)
            context['form'] = form
            if form.is_valid():
                # response =helpers.save_user(form)
                email = form.cleaned_data['email']
                name =form.cleaned_data['name']
                response = helpers.checkEmail(email)
                if response['status'] == 200:
                    # helpers.
                    password = form.cleaned_data['password']
                    user = User(email=email,name=name)
                    user.set_password(password)
                    user.save()
                    request.session.pop('veri2', None)
                    return redirect('login')
                context['message'] = response['message']           
        return render(request, 'user/Signup.html', context)
    return redirect('emailVerify')


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



@login_required(login_url='login')
def index(request):
    return render(request, 'user/Home.html')


@login_required(login_url='login')
def profileSetting(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        # print(request.user.password)
        stored_password = request.user.password
        input_password = request.POST.get('current_password', None)
        check = check_password(input_password,stored_password)
        if check:
            name = request.POST.get('name')
            email = request.POST.get('email')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')
            print(name, email, new_password, confirm_new_password)
    return render(request, 'user/Profile-setting.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')



def resendOTP(request):
    if request.method == 'GET':
        email =request.GET.get('email', None)
        if email is not None and len(email) > 0 :
            response_data  = helpers.resend_OTP_email(email)
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Email not None'})
    else:
        return JsonResponse({'error': 'Invalid request method'})



@csrf_exempt
def delete_profile_picture(request):
    default_image_url =  '/static/user/assets/svg/profile1-blue.svg'
    return JsonResponse({'default_image_url': default_image_url})