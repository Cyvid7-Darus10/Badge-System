from django import forms

class claimBadge(forms.Form):
    code  = forms.CharField(label="Code")
    name  = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")

class verifyBadge(forms.Form):
    serial  = forms.CharField(label="Serial Code")