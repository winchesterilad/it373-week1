from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, EVSU!")

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    context = {
        'Name': 'Joseph Clarence M. Hamtig',
        'Student_ID': '2023-26085'
    }
    return render(request, 'about.html', context)


