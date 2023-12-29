from django.core.mail import send_mail
from django.conf import settings


class Email:
    def send(generated_otp,input_email):
    # Send OTP to the user's email
        subject = 'Your OTP For Email Verification From Django Server'
        message = f'Your OTP is: {generated_otp}. Enter this code on the website to verify your email.'
        from_email = settings.EMAIL_HOST_USER  # Replace with your email address
        send_mail(subject, message, from_email, [input_email])

