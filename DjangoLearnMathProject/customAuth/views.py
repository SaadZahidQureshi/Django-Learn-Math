from django.shortcuts import render,redirect
from django.http import JsonResponse
from customAuth.sendEmail import Email
from .forms import OTPForm, SecondOTPForm
from customAuth import helpers
import random



# Create your views here.
def emailVerify(request):
    if (request.method == 'POST'):
        generated_otp = ''.join(random.choice('0123456789') for i in range(4))
        form = OTPForm(request.POST,generated_otp = generated_otp)
        if form.is_valid():
            input_email = form.cleaned_data['content']
            print(input_email)
            Email.send(generated_otp,input_email)
            form.save()
            # print(form.save())
            return render(request,'user/Code-Verify.html',{'email':input_email})
        else:
            print(form.errors)
    else:
        form = OTPForm()
    return render(request, 'user/Email-verify.html', {'form': form})
    
def codeVerify(request):
    if(request.method == 'POST'):
        print('sucess-1,', request.POST)
        form = SecondOTPForm(request.POST)
        print('sucess-2')
        if form.is_valid():
            print('sucess-3')
            print(form.cleaned_data)
            helpers.get_otp_verified_token
        return redirect('signup')

    else:
        form = SecondOTPForm()
    return render(request, 'user/Code-verify.html', {'form': form})


def signup(request):
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
    return render(request, 'user/Signup.html')