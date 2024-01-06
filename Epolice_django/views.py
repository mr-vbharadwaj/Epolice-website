from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from Epolice_django.models import Citizen, Complaints
from random import randint
# Create your views here.

def citizen_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            session_user = Citizen.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.email
                return redirect('citizen:home')
            else:
                return render(request, 'login.html', {'msg':'Invalid Password!!'})
        except:
            return render(request, 'login.html', {'msg':'Email does not exist, please register'})
                    

# def login_done(func):
#     def func(request):
#         if 'email' in request.session:
#             session_user = Citizen.objects.get(email = request.session['email'])
#             return func(request, {'session_user':session_user})
#         else:
#             return func(request)
#     return func


def login_required(fun):
    def func(request):
        if 'email' not in request.session:
            return redirect('citizen:login')
        else:
            return fun(request)
    return func

def home(request):
    if 'email' in request.session:
        session_user = Citizen.objects.get(email = request.session['email'])
        return render(request, 'index.html', {'session_user':session_user})
    else:
        return render(request, 'index.html')
        

@login_required
def complaint(request):
    if request.method == 'GET':
        return render(request, 'complaint.html')
    
@login_required
def about(request):
    if 'email' in request.session:
        session_user = Citizen.objects.get(email = request.session['email'])
        return render(request, 'about.html', {'session_user':session_user})
    else:
        return render(request, 'about.html')
    
@login_required
def services(request):
    if 'email' in request.session:
        session_user = Citizen.objects.get(email = request.session['email'])
        return render(request, 'services.html', {'session_user':session_user})
    else:
        return render(request, 'services.html')

@login_required
def contact(request):
    if 'email' in request.session:
        session_user = Citizen.objects.get(email = request.session['email'])
        return render(request, 'contact.html', {'session_user':session_user})
    else:
        return render(request, 'contact.html')
    
def citizen_logout(request):
    try:
        del request.session['email']
        return render(request, 'index.html', {'msg':'Successfully logged out!!'})
    except:
        return redirect('citizen:home')

@login_required
def status(request):
    # try:
        session_user = Citizen.objects.get(email = request.session['email'])
        if 'email' in request.session:
            complaints_data = Complaints.objects.filter(user_email = session_user)
            return render(request, 'status.html', {'session_user':session_user,'complaints':complaints_data})
        else:
            session_user = Citizen.objects.get(email = request.session['email'])
            return render(request, 'status.html', {'session_user':session_user})
    # except:
    #     return render(request, 'status.html', {'session_user':session_user})

@login_required
def submit_complaint(request):
    if request.method == 'GET':
        return render(request, 'complaint.html', {'msg':'Complaint submitted successfully'})
    else:
        try:
            session_user = Citizen.objects.get(email = request.session['email'])
            Complaints.objects.create(
                citizen_name = request.POST['full_name'],
                citizen_email = request.POST['email'],
                citizen_aadhaar = request.POST['aadhaar_number'],
                user_email = session_user,
                subject = request.POST['subject'],
                description = request.POST['complaintDetails'],
                time_of_incident = request.POST['date'],
                status = 'registered'
                )
            return render(request, 'complaint.html', {'msg':'Complaint submitted successfully!!!'})
        except:
            return render(request, 'complaint.html',{'msg':'Something went wrong, please try again!!'})

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
                global c_otp
                c_otp = randint(1000, 999_999)
                global citizen_data
                citizen_data = {
                    'full_name' : request.POST['full_name'],
                    'email' : request.POST['email'],
                    'password' : request.POST['password'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'aadhaar_card_no' : request.POST['aadhaar_card_no']
                }
                subject = 'Epolice registration'
                message = f"Hello {citizen_data['full_name']}, your otp to register on our site is {c_otp}"
                sender = settings.EMAIL_HOST_USER
                reciever = [request.POST['email']]
                send_mail(subject, message, sender, reciever)
                return render(request, 'otp.html')
            else:
                return render(request, 'register.html', {'msg':"Both passwords don't match"})

def citizen_otp(request):
        if str(c_otp) == request.POST['otp']:
            Citizen.objects.create(
                full_name = citizen_data['full_name'],
                email = citizen_data['email'],
                password = citizen_data['password'],
                mobile = citizen_data['mobile'],
                address = citizen_data['address'],
                aadhaar_card_no = citizen_data['aadhaar_card_no'],
            )
            return render(request, 'register.html', {'msg':'Account created successfully!!'})
        else:
            return render(request, 'register.html', {'msg':'Entered otp is invalid'})
    
def view_form(request, cid):
    # try:
        if 'email' in request.session:
            complaint_data = Complaints.objects.get(id = cid)
            # return HttpResponse(complaint_data)
            return render(request, 'preview.html', {'complaint':complaint_data})
        else:
            return redirect('citizen:login')
    # except:
    #     return HttpResponseBadRequest()
        
# def officer_page(request):
#     return render(request, 'officer_home.html')