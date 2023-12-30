from customAuth.models import OTP 
from django.utils import timezone
import secrets


def otp_verify(provided_otp, content):
    email_exist = OTP.objects.filter(content=content).exists()
    if email_exist:
            stored_otp = OTP.objects.filter(content=content).order_by('-created_at').first().code
            stored_timeout = OTP.objects.filter(content=content).order_by('-created_at').first().timeout
            if(timezone.now() > stored_timeout):
                print('OTP timeout! OTP expired.')
                return False
            elif(provided_otp==stored_otp):
                print('OTP matched successfully!!')
                return True
            else:
                print ("OTP Verification Failed")
                return False               
    else:
        print('Email Does not Exist')
        return False


def get_otp_verified_token(otp, content):
    token = f"{otp}_{content}_{secrets.token_urlsafe(16)}"
    return token
    # is_verified = otp_verify(otp,content)
    # if is_verified:
    # if True:
    #     token = f"{otp}_{content}_{secrets.token_urlsafe(16)}"
    #     return token
    # else:
    #     raise ValueError('OTP verification faild')




