from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.


def index(request):
    context = {
        'variable': "Nitin is great"
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, number=number, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent!')

    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


# Authentication functions
def signin(request):
    if request.method == "POST":
        # check that user login with correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        re_password = request.POST['re_password']
        email = request.POST['email']
        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return render(request, 'signup.html')
        if password != re_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        # creat users
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account has been successfully created Please Login.')

        return redirect('/signin')
    # else:
    #     return HttpResponse('404- Not found')
    return render(request, 'signup.html')
