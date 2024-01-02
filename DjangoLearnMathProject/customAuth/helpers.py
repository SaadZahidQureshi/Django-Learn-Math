from customAuth.models import User
from customAuth.models import OTP 
import datetime
import secrets


def otp_verify(provided_otp, content):
    email_exist = OTP.objects.filter(content=content).exists()
    if email_exist:
            stored_otp = OTP.objects.filter(content=content).order_by('-created_at').first().code
            stored_timeout = OTP.objects.filter(content=content).order_by('-created_at').first().timeout
            token = OTP.objects.filter(content=content).order_by('-created_at').first().verification_token


            if(datetime.datetime.now().time() < stored_timeout.time()):
                if(stored_otp == provided_otp):
                    OTP.objects.filter(content=content).update(used=True)
                    return {'token': token, 'status': 200, 'message':'OTP matched successfully!!'}
                else:
                    return {'status':406,'message':'OTP Verification Failed'} 
            else:
                return {'status': 408,'message':'OTP expired! To create new one '}              
    else:
        print('Email Does not Exist')
        return False


def get_otp_verified_token(otp, content):
    token = f"{otp}_{content}_{secrets.token_urlsafe(16)}"
    return token


def checkEmail(email):
    email_exist = User.objects.filter(email=email).exists()
    print(email_exist)
    if email_exist:
        return {'status': 403, 'message': 'Email Address already exist.'}
    else:
        return {'status': 200, 'message':'Email Registerrd successfully!!'}