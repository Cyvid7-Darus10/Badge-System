from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def claim(request):
    return HttpResponse("Claim!")

def verify(request):
    return HttpResponse("Verify!")