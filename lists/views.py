from django.shortcuts import render

# Create your views here.

def home():
    context = 'Hello world!'
    render(request, 'home.html', context)