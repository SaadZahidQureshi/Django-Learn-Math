from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from customAuth.models import UserVerification, Users
from django.contrib import messages
import random

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def forgotPassword(request):
    return render(request ,'user/Reset-Password.html')

def signup(request):
    obj = UserVerification.objects.all()
    if(request.method == 'POST'):

        input_name= request.POST.get('input-name')
        input_password= request.POST.get('input-password')
        return render(request, 'user/Login.html')
    return render(request, 'user/Signup.html')

def emailVerify(request):
    if(request.method == 'POST'):
        input_email = request.POST.get('email')
        if(input_email == ''):
            return render(request, 'user/Email-verify.html' )
        else:
            generated_otp = ''.join(random.choice('0123456789') for i in range(6))
            UserVerification.objects.create(email=input_email,otp=generated_otp, is_verified=False)

            # Send OTP to the user's email
            subject = 'Your OTP for Email Verification'
            message = f'Your OTP is: {generated_otp}. Enter this code on the website to verify your email.'
            from_email = 'saadzahid133204@gmail.com'  # Replace with your email address

            send_mail(subject, message, from_email, [input_email], fail_silently=False)
        return render(request, 'user/Code-verify.html')
    return render(request, 'user/Email-verify.html')

def codeVerify(request):
    if(request.method == 'POST'):
        user_otp = request.POST.get('input-otp')
        # print(user_otp)
        try:
            user_verification = UserVerification.objects.get(otp=user_otp, is_verified=False)
        except UserVerification.DoesNotExist:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'user/Code-verify.html',{'message': messages.get_messages(request)})
        user_verification.is_verified = True
        user_verification.save()
        return render( request, 'user/signup.html')
    return render(request, 'user/Code-verify.html')

def profileSetting(request):
    return render(request, 'user/Profile-Setting.html')

@csrf_exempt
def delete_profile_picture(request):
    default_image_url = '/static/user/assets/svg/profile1-blue.svg'
    print(default_image_url)
    return JsonResponse({'default_image_url': default_image_url})
