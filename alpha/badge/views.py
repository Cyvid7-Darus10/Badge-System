from django import forms
from django.shortcuts import render

class claimBadge(forms.Form):
    code  = forms.CharField(label="Code")
    name  = forms.CharField(label="Name")
    email = forms.CharField(label="Email")

class verifyBadge(forms.Form):
    serial  = forms.CharField(label="Serial Code")

def index(request):
    return render(request, "badge/home/home.html")

def claim(request):
    return render(request, "badge/claim/claim.html", {
        "form": claimBadge()
    })

def view_badge(request, code):
    return render(request, "badge/verify/view.html", {
        "code" : code 
    })

def verify(request):
    return render(request, "badge/verify/verify.html", {
        "form" : verifyBadge() 
    })