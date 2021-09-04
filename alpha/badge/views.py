from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "badge/home/home.html")

def claim(request):
    return render(request, "badge/claim/claim.html")

def verify(request, code = 0):
    # Checks whether code is valid
    # Code here

    return render(request, "badge/verify/verify.html", {
        "code" : code 
    })