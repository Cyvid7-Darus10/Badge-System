from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Badge, Guilder, Claimable, Claimed
from .support import random_serial
from .forms import claimBadge, verifyBadge
from datetime import datetime
import pytz

utc=pytz.UTC



# VIEWS

def index(request):
    css = [
        "/static/badge/home/styles.css"
    ]
    return render(request, "badge/home/home.html", {
        "csss" : css
    })

def claim(request):
    css = [
        "/static/badge/claim/styles.css"
    ]
    error = ""
    if request.method == "POST":
        form = claimBadge(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            try:
                guilder = Guilder.objects.get(email=email.lower())
                error = "Email is used already."
            except Guilder.DoesNotExist:
                try:
                    badge = Claimable.objects.get(code=code)
                    serial = random_serial()
                    try:
                        guilder = Guilder.objects.get(name=name.title(), email=email.lower())
                    except Guilder.DoesNotExist:
                        guilder = Guilder.objects.create(name=name.title(),email=email.lower())

                    try:
                        Claimed.objects.get(guilder=guilder,badge=badge)
                        error = "Already Claimed"
                    except Claimed.DoesNotExist:
                        curr_date = utc.localize(datetime.today())
                        if (badge.expires_on >= curr_date):
                            Claimed.objects.create(guilder=guilder,badge=badge,serial=serial)
                            url = reverse('badge:view_badge', kwargs={'code':serial})
                            return HttpResponseRedirect(url)
                        else:
                            error = "Expired Already"
                except Claimable.DoesNotExist:
                    error = "Not Found"
        else:
            return render(request, "badge/claim/claim.html", {
                "form": form,
                "csss" : css
            })

    return render(request, "badge/claim/claim.html", {
        "form": claimBadge(),
        "error": error,
        "csss" : css
    })

def view_badge(request, code):
    css = [
        "/static/badge/verify/view.css"
    ]
    
    try:
        badge = Claimed.objects.get(serial=code)
    except Claimed.DoesNotExist:
        badge = "Does Not Exist"

    return render(request, "badge/verify/view.html", {
        "badge" : badge,
        "csss" : css
    })

def verify(request):
    css = [
        "/static/badge/verify/styles.css"
    ]

    if request.method == "POST":
        form = verifyBadge(request.POST)
        if form.is_valid():
            url = reverse('badge:view_badge', kwargs={'code':form.cleaned_data["serial"]})
            return HttpResponseRedirect(url)
        else:
            return render(request, "badge/verify/verify.html", {
                "form" : form,
                "csss" : css
            })

    return render(request, "badge/verify/verify.html", {
        "form" : verifyBadge(),
        "csss" : css
    })