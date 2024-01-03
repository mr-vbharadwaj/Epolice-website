from django.shortcuts import render, redirect
from Epolice_django.models import Citizen
from random import randint
# Create your views here.

def citizen_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # try:
            session_user = Citizen.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.email
                return render(request, 'index.html', {'session_user':session_user})
            else:
                return render(request, 'login.html', {'msg':'Invalid Password!!'})
            
        # except:
        #     return render(request, 'login.html', {'msg':'Email is not registered, please signup!!'})
        
        

def login_required(fun):
    def func(request):
        if 'email' not in request.session:
            return redirect('login')
        else:
            return fun(request)
    return func


def home(request):
    return render(request, 'index.html')

@login_required
def complaint(request):
    if request.method == 'GET':
        return render(request, 'complaint.html')
    
# @login_required
def about(request):
    return render(request, 'about.html')

# @login_required
def services(request):
    return render(request, 'services.html')

# @login_required
def contact(request):
    return render(request, 'contact.html')

def citizen_logout(request):
    try:
        del request.session['email']
        return render(request, 'index.html', {'msg':'Successfully logged out!!'})
    except:
        return redirect('home')

# @login_required
def status(request):
    return render(request, 'status.html')

@login_required
def submit_complaint(request):
    return render(request, 'complaint.html', {'msg':'Complaint submitted successfully'})


def citizen_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        citizen_email = request.POST['email']
        try:
            citizen_obj = Citizen.objects.get(email = citizen_email)
            return render(request, 'register.html', {'msg':'Email aleady exists, please login'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global otp
                otp = randint(1000, 999_999)
                global citizen_data
                citizen_data = {
                    'full_name' : request.POST['full_name'],
                    'email' : request.POST['email'],
                    'password' : request.POST['password'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'aadhaar_card_no' : request.POST['aadhaar_card_no']
                }