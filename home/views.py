from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
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
