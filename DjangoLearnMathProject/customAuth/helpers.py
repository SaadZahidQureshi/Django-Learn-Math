from customAuth.sendEmail import Email
from customAuth.models import User
from customAuth.models import OTP 
from .forms import OTPForm,SecondOTPForm
import datetime
import secrets
import random


def otp_verify(request):
    form = SecondOTPForm(request.POST)
    content= form.clean_content()
    provided_otp = form.clean_code()
    email_exist = OTP.objects.filter(content=content).exists()
    if email_exist:
            stored_otp = OTP.objects.filter(content=content).order_by('-created_at').first().code
            stored_timeout = OTP.objects.filter(content=content).order_by('-created_at').first().timeout
            token = OTP.objects.filter(content=content).order_by('-created_at').first().verification_token
            if(datetime.datetime.now().time() < stored_timeout.time()):
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
    input_email = form.clean_content()
    generated_otp = ''.join(random.choice('0123456789') for i in range(4))
    token = get_token(generated_otp,input_email)
    timeout =  datetime.datetime.now() + datetime.timedelta(minutes=5)
    Email.send(generated_otp,input_email)
    form.save(code=generated_otp, verification_token=token, timeout = timeout)
    response={
        'email': input_email,
        'timeout':timeout
    }
    return response


def check_and_create_user(request):
    print(request)
    pass