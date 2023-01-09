from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def savecontact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if Contact.objects.filter(email=email).exists():
            messages.success(request,'Already Registered')
            return redirect('/contact/')
        data=Contact.objects.create(name=name,email=email,subject=subject,message=message)
        data.save()
        messages.success(request,'Sent Succesfully')
        return redirect('/contact/')