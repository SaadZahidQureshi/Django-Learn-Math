from typing import Any
from django import forms
from customAuth import models


class EmailVerificationForm(forms.ModelForm):
    # email = forms.EmailField()
    otp = forms.CharField(required=False)

    class Meta:
        model = models.UserVerification
        fields = '__all__'



class CodeVerificationForm(forms.ModelForm):
    # email = forms.EmailField()
    # otp = forms.IntegerField()

    class Meta:
        model = models.UserVerification
        fields = '__all__'
