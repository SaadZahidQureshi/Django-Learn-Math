from django.shortcuts import render,redirect
from .forms import OTPForm, SecondOTPForm
from customAuth.sendEmail import Email
from django.urls import reverse
from customAuth import helpers
import datetime
import random



# Create your views here.
def emailVerify(request):
    if (request.method == 'POST'):  
        form = OTPForm(request.POST)
        if form.is_valid():
            input_email = form.cleaned_data['content']
            generated_otp = ''.join(random.choice('0123456789') for i in range(4))
            token = helpers.get_otp_verified_token(generated_otp,input_email)
            timeout =  datetime.datetime.now() + datetime.timedelta(minutes=2)
            Email.send(generated_otp,input_email)
            form.save(email=input_email, generated_otp=generated_otp, token=token, timeout = timeout)
            return redirect(reverse('codeVerify') + f'?email={input_email}')
        else:
            return render(request, 'user/Email-verify.html', {'form': form})
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    
def codeVerify(request):
    input_email = request.GET.get('email','')
    if(request.method == 'POST'):
        form = SecondOTPForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            content = form.cleaned_data['content']
            is_verified = helpers.otp_verify(code, content)
            if is_verified:
                return redirect(reverse('signup')+ f'?email={input_email}')
            else:
                return render(request, 'user/Code-verify.html', {'form': form,'email':input_email})
        else:
            return render(request, 'user/Code-verify.html', {'form': form,'email':input_email})
    else:
        form = SecondOTPForm()
    return render(request, 'user/Code-verify.html', {'form': form,'email':input_email})


def signup(request):
    input_email = request.GET.get('email','')

    # if(request.method == 'POST'):
    #     input_name= request.POST.get('input-name')
    #     input_email =request.POST.get('input-email')
    #     input_password= request.POST.get('input-password')
    #     input_confirm_password= request.POST.get('input-confirm-password')
    #     print(input_name, input_email,input_password, input_confirm_password)

    #     obj = UserVerification.objects.filter(email =input_email).first()
    #     print(obj.is_verified)
    #     # verification =obj.is_verified
    #     if(input_password == input_confirm_password):
    #         Users.objects.create(user_name = input_name, user_email= input_email, user_password= input_password, is_verified=obj )
    #     else:
    #         pass

    #     return render(request, 'user/Login.html')
    return render(request, 'user/Signup.html', {'email':input_email})