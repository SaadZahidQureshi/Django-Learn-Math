from .forms import OTPForm, SecondOTPForm, UserForm, CustomAuthenticationForm, UpdateUserForm, resetPasswordForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from customAuth.models import User
from django.urls import reverse
from customAuth import helpers


# Create your views here.
def emailVerify(request):
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    acc_type = request.GET.get('type', None)
    if (request.method == 'POST'):
        form = OTPForm(request.POST)
        if form.is_valid():

            response= helpers.send_email_save_record(request,acc_type)
            context = {
                'form': form,
                'acc_type': acc_type
            }
            if response.__contains__('error'):
                context['error'] = response['error']
                return render(request, 'user/Email-verify.html', context)

            request.session['veri1'] = True
            return redirect(reverse('codeVerify') + f'?email={response["email"]}&type={acc_type}')
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form, 'acc_type': acc_type})
    
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
                    acc_type = response['acc_type']
                    request.session.pop('veri1',None)
                    request.session['veri2'] = True
                    if(acc_type == 'forgot'):
                        return redirect(reverse('resetPassword') + f'?email={content}')
                    return redirect(reverse('signup') + f'?email={content}'+f"&token={token}")
                context['message'] = response['message']
        # context['acc_type'] = acc_type
        return render(request, 'user/Code-verify.html', context=context)
    return redirect('emailVerify')

def signup(request):
    if request.user.is_authenticated:
        return redirect('user-dashboard')

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
                email = form.cleaned_data['email']
                name =form.cleaned_data['name']
                response = helpers.checkEmail(email)
                if response['status'] == 200:
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
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user-dashboard')  # Redirect to your home page or any other desired page
            else:
                message = 'User does not exist!'
                return render(request, 'user/Login.html', {'form': form, 'message': message})
        else:
            message = 'Form Validations faild!'
            return render(request, 'user/Login.html', {'form': form, 'message': message})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/Login.html', {'form': form})

@login_required(login_url='login')
def index(request):
    return render(request, 'user/Home.html')

@login_required(login_url='login')
def profileSetting(request):
    user = request.user
    form = UpdateUserForm()

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            old_password = request.POST.get('password', '')
            
            if old_password:
                if check_password(old_password, user.password):
                    new_password = request.POST['new_password']
                    confirm_new_password = request.POST['confirm_new_password']

                    if new_password == confirm_new_password:
                        user.set_password(new_password)
                        user.save()
                        # Ensure the user stays logged in after the password change
                        update_session_auth_hash(request, user)
                        messages.success(request, 'Your password has been changed successfully')
                        return redirect('profileSetting')
                    else:
                        messages.error(request, 'New passwords do not match')
                        return redirect('profileSetting')
                else:
                    messages.error(request, 'Incorrect old password')
                    return redirect('profileSetting')

            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profileSetting')
        else:
            messages.error(request, 'Error in the form submission')
            print(form.errors)

    return render(request, 'user/Profile-setting.html', {"form": form})

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

@login_required(login_url='login')
def delete_profile_picture(request):
    user = request.user
    user.profile_image = 'profile1-blue.svg'
    user.save()
    messages.success(request,'Your profile Pic is updated successfully')
    return redirect('profileSetting')
  
def resetPassword(request):
    key = request.session.get('veri2', None)
    context={
        'form': resetPasswordForm(),
        'email' : request.GET.get('email', None)
    }
    
    if key:
        if(request.method == 'POST'):
            form = resetPasswordForm(request.POST)
            if form.is_valid():
                email = context['email']
                # print(request.POST)
                response =  helpers.reset_passwrod(request.POST, email)
                if(response.__contains__('success')):
                    context['success'] = response['success']
                    return redirect('login')
                    return render(request, 'user/Reset-Password.html', context)
            context['form']= form
        return render(request, 'user/Reset-Password.html', context)
    else:
        return redirect('emailVerify')
