
from customAuth.models import OTP 
import secrets


def otp_verify(provided_otp, content):
    try:
        stored_otp = OTP.objects.get(content= content).code
        return provided_otp==stored_otp
    except OTP.DoesNotExist:
        print ("OTP Verification Failed")
        return False

def get_otp_verified_token(otp, content):
    is_verified = otp_verify(otp,content)
    if is_verified:
        token = f"{otp}_{content}_{secrets.token_urlsafe(16)}"
        print('token ->',token)
        return token
    else:
        raise ValueError('OTP verification faild')