from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/home.html")

def claim(request):
    return render(request, "claim/claim.html")

def verify(request, code):
    return render(request, "verify/verify.html", {
        "code" : code 
    })