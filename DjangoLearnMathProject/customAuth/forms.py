from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from customAuth.models import OTP
from customAuth import helpers
from django import forms
import datetime
import re



class OTPForm(forms.ModelForm):
    # email = forms.EmailField()
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
        
        # def clean_code(self):
        #     code = self.cleaned_data['code']
        #     if not re.match(r'^\d{4}$', code):
        #         raise forms.ValidationError('OTP must be a 4-digit number.')
        #     return code
        

        # def clean(self):
        #     cleaned_data = super().clean()
        #     content = cleaned_data.get('content')
        #     code = cleaned_data.get('code')

        #     token = helpers.get_otp_verified_token(code=code, content=content)
            

                  


    def __init__(self,  *args, **kwargs):
        self.otp =kwargs.pop('generated_otp', None)
        super(OTPForm,self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(OTPForm, self).save(commit=False)
        obj.code = self.otp
        obj.timeout = datetime.datetime.now() + datetime.timedelta(minutes=2)
        if commit:
            obj.save()
        return obj
    





class SecondOTPForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = OTP
        fields = ["content","code"]
    
    def clean_content(self):
        content = self.cleaned_data['content']
        print(content)
        try:
            validate_email(content)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")
        return content
    
    def clean_code(self):
        code = self.cleaned_data['code']
        print(code)
        print('testing...')
        if not re.match(r'^\d{4}$', code):
            raise forms.ValidationError('OTP must be a 4-digit number.')
        return code
    

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        code = cleaned_data.get('code')
        token = helpers.get_otp_verified_token(code,content)
        return token

    


