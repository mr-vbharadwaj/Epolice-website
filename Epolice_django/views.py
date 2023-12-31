from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def complain(request):
    return render(request, 'complain.html')