from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from customAuth.models import OTP, User
from django import forms
import re

class StandardForm(forms.ModelForm):
    def save(self, commit= True, *args, **kwargs):
        instance = super().save(False)
        model_fields = []
        for field in self._meta.model._meta.get_fields():
            model_fields.append(field.name)

        for key, value in kwargs.items():
            if key in model_fields:
                setattr(instance,key,value)

        if commit:
            instance.save()
        return instance
        
class OTPForm(StandardForm):
    class Meta:
        model = OTP
        fields = ["content"]
    
    def clean_content(self):
        content = self.cleaned_data['content']
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
        code = self.cleaned_data['code']
        if not re.match(r'^\d{4}$', code):
            # here it prints error statement but no raising the error 
            raise forms.ValidationError('OTP must be a 4-digit number.')
        return code
       
class UserForm(StandardForm):
    # password=forms.CharField()
    confirm_password=forms.CharField()
    class Meta:
        model=User
        fields=('name','email','password')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(symbol in name for symbol in ['@', '.', '-', '+']):
            raise forms.ValidationError('Symbols @/./-/+ are not allowed in username.')
        return name


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print(password, confirm_password)
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    
class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean_content(self):
        email = self.cleaned_data['email']
        print(email)
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email
    