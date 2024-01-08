from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from customAuth.models import OTP, User
from django import forms
import re


class StandardForm(forms.ModelForm):
    def save(self,commit=True,**kwargs):
        ins = super().save(commit=False)
        used_arguments = kwargs
        if 'commit' in used_arguments:
            used_arguments.pop('commit')
        for arg, value in used_arguments.items():
            if hasattr(ins, arg):
                setattr(ins, arg, value)
            else:
                raise ValueError(f"{arg} does not exists in {ins.__class__.__name__}")
        if commit:
            ins.save()
        return ins


class OTPForm(StandardForm):
    class Meta:
        model = OTP
        fields = ["content"]
    
    def clean_content(self):
        content = self.data['content']
        try:
            validate_email(content)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")
        return content
    

class SecondOTPForm(StandardForm):
    class Meta:
        model = OTP
        fields = ["content","code"]
    
    def clean_content(self):
        content = self.cleaned_data['content']
        try:
            validate_email(content)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")
        return content
    
    def clean_code(self):
        code = self.data['code']
        code  = code.strip()
        print(code)
        if not re.match(r'^\d{4}$', code):
            # here it prints error statement but no raising the error 
            raise forms.ValidationError('OTP must be a 4-digit number.')
        return code
       

class UserForm(StandardForm):
    password=forms.CharField()
    confirm_password=forms.CharField()
    class Meta:
        model=User
        fields=('name','email','password')


    def clean_email(self):
        email = self.data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email


    def clean_name(self):
        name = self.data['name']
        if any(symbol in name for symbol in ['@', '.', '-', '+']):
            raise forms.ValidationError('Symbols @/./-/+ are not allowed in username.')
        return name


    def clean(self):
        password = self.data['password']
        confirm_password = self.data['confirm_password']
        
        if((password or confirm_password )== None):
            raise forms.ValidationError('This field is required!')

        if (password != confirm_password):
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        else:
            if(len(password) < 6):
                raise forms.ValidationError('Password too short. Must be at least 6 characters')
    

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean_content(self):
        email = self.data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email
    

class UpdateUserForm(forms.ModelForm):
        
    class Meta:
        model = User
        fields =['name', 'email', 'profile_image']
        
    def clean_email(self):
        email = self.data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email


    def clean_name(self):
        name = self.data['name']
        if any(symbol in name for symbol in ['@', '.', '-', '+']):
            raise forms.ValidationError('Symbols @/./-/+ are not allowed in username.')
        return name


