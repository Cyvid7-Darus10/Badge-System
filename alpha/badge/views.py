from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Badge, Guilder, Claimable, Claimed
from .support import random_serial

class claimBadge(forms.Form):
    code  = forms.CharField(label="Code")
    name  = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")

class verifyBadge(forms.Form):
    serial  = forms.CharField(label="Serial Code")

# VIEWS
def index(request):
    return render(request, "badge/home/home.html")

def claim(request):
    badge = "Does Not Exist"
    if request.method == "POST":
        form = claimBadge(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            try:
                badge = Claimable.objects.get(code=code)
                serial = random_serial()
                try:
                    guilder = Guilder.objects.get(name=name, email=email)
                    email = Guilder.objects.get(email=email)
                except Guilder.DoesNotExist:
                    guilder = Guilder.objects.create(name=name,email=email)
                try:
                    Claimed.objects.get(guilder=guilder,badge=badge)
                    badge = "Already Claimed"
                except Claimed.DoesNotExist:
                    Claimed.objects.create(guilder=guilder,badge=badge,serial=serial)
                    url = reverse('badge:view_badge', kwargs={'code':serial})
                    return HttpResponseRedirect(url)
            except Claimable.DoesNotExist:
                badge = "Not Found"
        else:
            return render(request, "badge/claim/claim.html", {
                "form": form
            })

    return render(request, "badge/claim/claim.html", {
        "form": claimBadge(),
        "badge": badge
    })

def view_badge(request, code):
    # Check the code in the db
    try:
        badge = Claimed.objects.get(serial=code)
    except Claimed.DoesNotExist:
        badge = "Does Not Exist"
    
    
    return render(request, "badge/verify/view.html", {
        "badge" : badge
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