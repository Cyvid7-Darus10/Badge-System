from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/home.html")

def claim(request):
    return render(request, "claim/claim.html")

def verify(request, code):
    # Checks whether code is valid
    # Code here
    
    return render(request, "verify/verify.html", {
        "code" : code 
    })