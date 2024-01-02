from django.shortcuts import render, redirect
from Epolice_django.models import Citizen
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            session_user = Citizen.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.email
                return render(request, 'index.html', {'user_data':session_user})
            else:
                return render(request, 'login.html', {'msg':'Password is not valid!!'})
        except:
            return render(request, 'login.html', {'msg':'Entered email does not exist, please register!!'})
        

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
    
@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def services(request):
    return render(request, 'services.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def logout(request):
    del request.session['email']
    return render(request, 'index.html')