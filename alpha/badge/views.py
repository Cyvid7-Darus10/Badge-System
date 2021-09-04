from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "badge/home/home.html")

def claim(request):
    return render(request, "badge/claim/claim.html")

def view_badge(request, code = 0):
    return render(request, "badge/verify/view.html", {
        "code" : code 
    })

def verify(request):
    return render(request, "badge/verify/verify.html")