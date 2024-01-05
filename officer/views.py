from django.shortcuts import render, redirect
from Epolice_django.models import Complaints
from officer.models import Officer
from django.http import HttpResponse

# Create your views here.

def officer_login_required(func):
    def fun(request):
        if 'email' in request.session:
            return func(request)
        else:
            return redirect('officer:officer_login')
    return fun

def officer_home(request):
    if 'email' in request.session:
        user_email = request.session['email']
        session_user = Officer.objects.get(officer_email = user_email)
        return render(request, 'officer_index.html', {'session_user':session_user})
    else:
        return render(request, 'officer_index.html')

@officer_login_required
def view_complaints(request):
    complaints_data = Complaints.objects.all()
    return render(request, 'view_complaints.html', {'complaints':complaints_data})

def officer_login(request):
    if request.method == 'GET':
        return render(request, 'officer_login.html')
    else:
        try:
            user_email = request.POST['email']
            session_user = Officer.objects.get(officer_email = user_email)
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.officer_email
                return redirect('officer:officer_home')
            else:
                return render(request, 'officer_login.html', {'msg':'Password is invalid'})
        except:
            return render(request, 'officer_login.html', {'msg':'You are not registered, please contact admin to register!!'})

@officer_login_required
def complaint_edit(request, cid):
    complaints_data = Complaints.objects.get(id = cid)
    return render(request, 'complaint_edit.html', {'complaint':complaints_data})

@officer_login_required
def save_edit(request, cid):
    complaints_data = Complaints.objects.get(id = cid)
    complaints_data.status = request.POST['status']
    complaints_data.save()
    return render(request, 'complaint_edit.html', {'complaint':complaints_data,'msg':'Complaint was successfully edited'})

def officer_logout(request):
    del request.session['email']
    return redirect('officer:officer_home')