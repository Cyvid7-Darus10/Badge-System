from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Badge, Guilder, Claimable, Claimed
from .support import random_serial, get_if_exists
from .forms import claimBadge, verifyBadge
from django.utils import timezone
from .encryption import encrypt, decrypt

js = []
css = []

def index(request):
    css = [
        "/static/badge/home/styles.css"
    ]
    return render(request, "badge/home/home.html", {
        "csss" : css,
        "jss"  : js
    })

def claim(request):
    css = [
        "/static/badge/claim/styles.css"
    ]
    error = ""
    form = ""
    if request.method == "POST":
        form = claimBadge(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            name = form.cleaned_data["name"]
            email = encrypt(form.cleaned_data["email"].lower())

            guilder = get_if_exists(Guilder, **{'name':name.title(), 'email':email})
            guilder_email = get_if_exists(Guilder, **{'email':email})

            if not guilder and not guilder_email:
                guilder = Guilder.objects.create(name=name.title(),email=email)
            elif not guilder and guilder_email:
                error = "Email is Already Used"

            if guilder:
                badge = get_if_exists(Claimable, **{'code':code})
                claimed = get_if_exists(Claimed, **{'guilder':guilder,'badge':badge})
                if claimed:
                    error = "Badge is Claimed Already"
                elif badge:
                    serial = random_serial()
                    curr_date = timezone.now()
                    if (badge.expires_on >= curr_date):
                        Claimed.objects.create(guilder=guilder,badge=badge,serial=serial)
                        url = reverse('badge:view_badge', kwargs={'code':serial})
                        return HttpResponseRedirect(url)
                    error = "Badge is Already Expired"
                else:
                    error = "Badge is not Found"
        
    form = form if form != "" else claimBadge()

    return render(request, "badge/claim/claim.html", {
        "form": form,
        "error": error,
        "csss" : css,
        "jss"  : js
    })

def view_badge(request, code):
    css = [
        "/static/badge/verify/view.css"
    ]

    js = [
        "/static/badge/verify/view.js"
    ]

    badge = get_if_exists(Claimed, **{'serial':code})
    if not badge:
        badge = "Does Not Exist"

    return render(request, "badge/verify/view.html", {
        "badge" : badge,
        "csss" : css,
        "jss"  : js
    })

def verify(request):
    css = [
        "/static/badge/verify/styles.css"
    ]
    
    form = ""
    if request.method == "POST":
        form = verifyBadge(request.POST)
        if form.is_valid():
            url = reverse('badge:view_badge', kwargs={'code':form.cleaned_data["serial"]})
            return HttpResponseRedirect(url)

    form = form if form != "" else verifyBadge()

    return render(request, "badge/verify/verify.html", {
        "form" : form,
        "csss" : css,
        "jss"  : js
    })


def contact(request):
    css = [
        "/static/badge/contact/styles.css"
    ]

    return render(request, "badge/contact/contact.html", {
        "csss" : css,
        "jss"  : js
    })