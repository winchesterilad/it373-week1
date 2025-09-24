from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, EVSU!")

def home(request):
    return render(request, "home.html", {"title": "Home"})

def about(request):
    context = {
        'Name': 'Winchester T. Ilad',
        'Student_ID': '2023-25610'
    }
    return render(request, 'about.html', context)

