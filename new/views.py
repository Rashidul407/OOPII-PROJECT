from http.client import HTTPResponse
from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        
    
    return render(request,'contact.html')

def showdata(request):
    contacts = Contact().objects.all()
    print(type(contact))
    for i in contacts:
        print(i)
    return render(request,'showdata.html')
