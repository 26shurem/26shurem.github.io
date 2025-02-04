from email.headerregistry import Address
from lib2to3.fixes.fix_input import context
from types import MemberDescriptorType

from django.contrib.auth import authenticate
from django.db.backends.ddl_references import Reference
from django.shortcuts import render ,redirect
from django.contrib import (messages)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.template.context_processors import request
from .models import Contact, MembershipPlan, Enrollment, Trainer


# Create your views here.
def home(request):
    return render(request, "myapp/home.html", {})
def signup(request):
    if request.method=="POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if len(username) > 10 or len(username)< 10:
            messages.info(request, "Phone number must be 10 digits")
            return redirect('signup')
        if pass1 != pass2:
            messages.info(request,"Passwords Are Not Matching")
            return redirect('signup')

        try:
            if User.objects.get(username=username()):
                messages.info(request,"Phone Number is Taken")
                return redirect('signup')
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email()):
                messages.info(request, "Email is Taken")
                return redirect('signup')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request, "User is created - Please login")
        return redirect('/login_user')

    return render(request, "myapp/signup.html", {})
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request,"login Succesfull!")
            return redirect('/')
        else:

            messages.success(request, "Invalid Creditials")
            return redirect("/login_user")
    return render(request, "myapp/login_user.html", {})

def logout_user(request):
    logout(request)
    messages.success(request,"logout Succesful")
    return redirect("/login_user")
def contacts(request):
    if request.method=="POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        number = request.POST.get("fullname")
        desc = request.POST.get("desc")
        myquery = Contact(name=name,email=email,phonenumber=number,description = desc)
        myquery.save()
        messages.info(request,"Thanks")
        return redirect(('/contact'))
    return render(request,'myapp/contact.html')
def Enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try again")
        return redirect('/login_user')
    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    if request.method == "POST":
        context = {"Membership", Membership,"SelectTrainer",SelectTrainer}
        FullName = request.POST.get("FullName")
        email = request.POST.get("email")
        PhoneNumber = request.POST.get("PhoneNumber")
        gender = request.POST.get("gender")
        DOB = request.POST.get("DOB")
        member=request.POST.get("member")
        trainer = request.POST.get("trainer")
        refrence = request.POST.get("refrence")
        address = request.POST.get("address")
        query = Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber = PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=refrence,Address=address)
        query.save()
        messages.success(request, "Thanks for Joining!")
        return redirect('/join')
    return render(request, "myapp/enroll.html",context)