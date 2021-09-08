from django import forms
from captcha.fields import CaptchaField

class claimBadge(forms.Form):
    code  = forms.CharField(label="Code")
    name  = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    captcha = CaptchaField()

class verifyBadge(forms.Form):
    serial  = forms.CharField(label="Serial Code")
    captcha = CaptchaField()