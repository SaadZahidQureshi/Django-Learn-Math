from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from customAuth.models import UserVerification, Users
from django.contrib import messages
from .forms import EmailVerificationForm, CodeVerificationForm
import random
from django.conf import settings

# Create your views here.

def login(request):
    print('')
    input_email = request.POST.get('input-email')
    input_password = request.POST.get('input-password')
    print(input_email,input_password)
    return render(request, 'user/login.html')

def forgotPassword(request):
    return render(request ,'user/Reset-Password.html')

def emailVerify(request):
    if (request.method == 'POST'):
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            print("Form is saved successfully")
            generated_otp = ''.join(random.choice('0123456789') for i in range(6))
            instance = form.save(commit=False)
            instance.otp = generated_otp
            instance.save()
            
            input_email = form.cleaned_data['email']
            UserVerification.objects.create(email = input_email, otp = generated_otp)
            sendEmail(generated_otp,input_email)
            return render(request,'user/Code-Verify.html',{'email':input_email})
        else:
            print(form.errors)
    else:
        form = EmailVerificationForm()
    return render(request, 'user/Email-verify.html', {'form': form})


def codeVerify(request):
    if(request.method == 'POST'):
        form = CodeVerificationForm(request.POST)
        print('success-1')
        if form.is_valid():
            print('success-2')
            input_email = form.cleaned_data['email']
            input_otp = form.cleaned_data['otp']
            user_record =UserVerification.objects.get(email=input_email)
            print(user_record)
            if(user_record.otp == input_otp):
                return JsonResponse({'success': True, 'email': input_email})
            else:
                return JsonResponse({'success': False})
            # return render(request, 'user/Signup.html',{'email': input_email})
        else:
            print(form.errors)
    else:
        form = CodeVerificationForm()
    return render(request, 'user/Code-verify.html', {'form': form})

def signup(request):
    if(request.method == 'POST'):
        input_name= request.POST.get('input-name')
        input_email =request.POST.get('input-email')
        input_password= request.POST.get('input-password')
        input_confirm_password= request.POST.get('input-confirm-password')
        print(input_name, input_email,input_password, input_confirm_password)

        obj = UserVerification.objects.filter(email =input_email).first()
        print(obj.is_verified)
        # verification =obj.is_verified
        if(input_password == input_confirm_password):
            Users.objects.create(user_name = input_name, user_email= input_email, user_password= input_password, is_verified=obj )
        else:
            pass

        return render(request, 'user/Login.html')
    return render(request, 'user/Signup.html')

def sendEmail(generated_otp,input_email):
    # Send OTP to the user's email
    subject = 'Your OTP For Email Verification From Django Server'
    message = f'Your OTP is: {generated_otp}. Enter this code on the website to verify your email.'
    from_email = settings.EMAIL_HOST_USER  # Replace with your email address
    send_mail(subject, message, from_email, [input_email])

def profileSetting(request):
    return render(request, 'user/Profile-Setting.html')

@csrf_exempt
def delete_profile_picture(request):
    default_image_url = '/static/user/assets/svg/profile1-blue.svg'
    print(default_image_url)
    return JsonResponse({'default_image_url': default_image_url})
