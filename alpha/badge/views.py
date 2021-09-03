from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def claim(request):
    return render(request, "claim/index.html")

def verify(request, code):
    return render(request, "verify/index.html", {
        "code" : code 
    })