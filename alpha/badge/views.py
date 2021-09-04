from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class claimBadge(forms.Form):
    code  = forms.CharField(label="Code")
    name  = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")

class verifyBadge(forms.Form):
    serial  = forms.CharField(label="Serial Code")

def index(request):
    return render(request, "badge/home/home.html")

def claim(request):
    if request.method == "POST":
        form = claimBadge(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
        else:
            return render(request, "badge/claim/claim.html", {
                "form": form
            })


    return render(request, "badge/claim/claim.html", {
        "form": claimBadge()
    })

def view_badge(request, code):
    # Check the code in the db
    return render(request, "badge/verify/view.html", {
        "code" : code 
    })

def verify(request):
    if request.method == "POST":
        form = verifyBadge(request.POST)
        if form.is_valid():
            url = reverse('badge:view_badge', kwargs={'code':form.cleaned_data["serial"]})
            return HttpResponseRedirect(url)
        else:
            return render(request, "badge/verify/verify.html", {
                "form" : form 
            })

    return render(request, "badge/verify/verify.html", {
        "form" : verifyBadge() 
    })