from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def messages(request):
    return render(request,'home.html')

def click(request):
    return render(request,'click.html')

def search(request):
    return render(request,'search.html')

def impress(request):
    return render(request,'impress.html')