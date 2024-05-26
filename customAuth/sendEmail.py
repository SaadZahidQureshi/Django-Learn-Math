# from django.core.mail import send_mail
# from django.conf import settings


# class Email:
#     def send(generated_otp,input_email):
#         if(input_email is not None):
#         # Send OTP to the user's email
#             subject = 'Your OTP For Email Verification From Django Server'
#             message = f'Your OTP is  {generated_otp}. Enter this code on the website to verify your email.'
#             from_email = settings.EMAIL_HOST_USER  # Replace with your email address
#             send_mail(subject, message, from_email, [input_email])
#         else:
#             print('email is None')

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
class Email:
    def send(code,email):
        if email is not None:
            subject = 'Email Verification for Signup'
            html_message = render_to_string('user/Email.html', {'code': code})
            # message = f'Your OTP is: {code}. Enter this code on the website to verify your email.'
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = email
            send_mail(subject, plain_message, from_email, [to],html_message=html_message)
        else:
            print('email is None')