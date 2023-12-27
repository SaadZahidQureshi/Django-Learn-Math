from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from customAuth.models import UserVerification, Users
from django.contrib import messages
import random
from django.conf import settings
# from .utils import
# import yagmail

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
    if(request.method == 'POST'):
        input_email = request.POST.get('email')
        if(input_email == ''):
            return render(request, 'user/Email-verify.html' )
        else:
            generated_otp = ''.join(random.choice('0123456789') for i in range(6))
            UserVerification.objects.create(email=input_email,otp=generated_otp, is_verified=False)
            sendEmail(generated_otp, input_email)
        return render(request, 'user/Code-verify.html', {'email': input_email})
    return render(request, 'user/Email-verify.html')

def codeVerify(request):
    if(request.method == 'POST'):
        input_otp = request.POST.get('input-otp')
        input_email = request.POST.get('input-email')
        global n
        n = str(input_email)
        user_record = UserVerification.objects.filter(email=input_email).first()
        # print(user_record.otp)
        if (str(user_record.otp) == str(input_otp)):
            user_record.is_verified = True
            user_record.save()
            return JsonResponse({'success': True, 'email': input_email})
            
        else:
            return JsonResponse({'success': False})
            # messages.error(request, 'Invalid OTP. Please try again.')
            # return render(request, 'user/Code-verify.html',{'message': messages.get_messages(request)})
        
    return render(request, 'user/Code-verify.html')

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
    return render(request, 'user/Signup.html',{'email':n})

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
