from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from customAuth.models import OTP
from customAuth import helpers
from django import forms
import datetime
import re



class OTPForm(forms.ModelForm):
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
    
    def save(self, commit=True, *args, **kwargs):
        # Extract additional parameters from kwargs
        email = kwargs.pop('email', None)
        generated_otp = kwargs.pop('generated_otp', None)
        token = kwargs.pop('token', None)
        timeout = kwargs.pop('timeout',None)
        # Call the superclass's save method to save the form data
        instance = super(OTPForm, self).save(commit=False)

        # Save additional parameters to the instance
        instance.content = email
        instance.code = generated_otp
        instance.verification_token = token
        instance.timeout = timeout

        if commit:
            instance.save()
        return instance
    

class SecondOTPForm(forms.ModelForm):
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
    

    # def clean(self):
    #     cleaned_data = super().clean()
    #     content = cleaned_data.get('content')
    #     code = cleaned_data.get('code')
    #     token = helpers.get_otp_verified_token(code,content)
    #     return token

    


