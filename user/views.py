from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def complaint_view(request):
    return render(request, 'complaint.html')
def contact_view(request):
    return render(request, 'contact.html')
def services_view(request):
    return render(request, 'services.html')