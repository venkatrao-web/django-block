from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World! This is the home page of the blog.")

def home1(request):
    return render(request, 'home1.html')