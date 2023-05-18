from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'auth_app/register.html')
    
    else:
       fn = request.POST['firstname']
       ln = request.POST['lastname']
       email = request.POST['email']
       username = request.POST['username']
       pswd = request.POST['password']

    #    print('********')
    #    print(request.POST['firstname'])
    #    print(make_password(pswd))

       User.objects.create_user(first_name=fn, last_name=ln, email=email, username=username, password=pswd)

       return redirect('authapp-login')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'auth_app/login.html')
    
    else:
        username = request.POST['username']
        pswd = request.POST['password']

        user = authenticate(request, username=username, password=pswd)
        if user is not None:
            login(request, user)
            # print('##########')
            # print(request.GET.get('next'))
            next_url = request.GET.get('next')
            if next_url is not None:
                return redirect(next_url)
            return redirect('main-home')
        else:
            return redirect('authapp-login')
        
def logout_user(request):

    logout(request)

    return redirect('authapp-login')






