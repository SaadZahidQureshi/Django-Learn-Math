from .forms import OTPForm,SecondOTPForm
from customAuth.sendEmail import Email
from customAuth.models import User
from customAuth.models import OTP 
from django.utils import timezone
import datetime
import secrets
import random


def otp_verify(request):
    print('otp verification request data : ',request.POST)
    # form = SecondOTPForm(request.POST)
    content= request.POST.get('content', None)
    provided_otp = request.POST.get('code', None)
    email_exist = OTP.objects.filter(content=content).exists()
    if email_exist:
            stored_otp = OTP.objects.filter(content=content).order_by('-created_at').first().code
            stored_timeout = OTP.objects.filter(content=content).order_by('-created_at').first().timeout
            token = OTP.objects.filter(content=content).order_by('-created_at').first().verification_token

            # record = OTP.objects.filter(content=content).order_by()
            # token = OTP.objects.filter(content=content).order_by('-created_at').first().
            # print('stored otp ->', stored_otp)
            # print('stored time ->', timezone.localtime(stored_timeout))
            # print('current time ->', datetime.datetime.now().time() )

            convertedtime = timezone.localtime(stored_timeout)
            if(datetime.datetime.now().time() < convertedtime.time()):
                if(stored_otp == provided_otp):
                    OTP.objects.filter(content=content).update(used=True)
                    return {'token': token,'content' :  content, 'status': 200, 'message':'OTP matched successfully!!'}
                else:
                    return {'status':406,'message':'OTP Verification Failed'} 
            else:
                return {'status': 408,'message':'OTP expired! To create new one '}              
    else:
        print('Email Does not Exist')
        return False


def get_token(otp, content):
    token = f"{otp}_{content}_{secrets.token_urlsafe(16)}"
    return token


def checkEmail(email):
    email_exist = User.objects.filter(email=email).exists()
    if email_exist:
        return {'status': 403, 'message': 'Email Address already exist.'}
    else:
        return {'status': 200, 'message':'Email Registerrd successfully!!'}
    

def send_email_save_record(request):
    form = OTPForm(request.POST)
    input_email = request.POST.get('content', None)
    generated_otp = ''.join(random.choice('0123456789') for i in range(4))
    token = get_token(generated_otp,input_email)
    timeout =  datetime.datetime.now() + datetime.timedelta(minutes=3)
    Email.send(generated_otp,input_email)
    form.save(code=generated_otp, verification_token=token, timeout = timeout)
    response={
        'email': input_email,
    }
    return response



def save_user(form):
    name =form.cleaned_data['name']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    response = checkEmail(email)

    if response['status'] == 200:
        user = User(email=email,name=name)
        user.set_password(password)
        user.save()
    return response    




def check_and_create_user(request):
    print(request)
    pass


def resend_OTP_email(email):
    generated_otp = ''.join(random.choice('0123456789') for i in range(4))
    token = get_token(generated_otp,email)
    timeout =  datetime.datetime.now() + datetime.timedelta(minutes=3)
    Email.send(generated_otp,email)