from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method =='POST':
        firstname=request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('index')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                messages.info(request,'sign up successfully')
                return redirect('loginpage')
        else:
            return redirect('index')
    else:
            return redirect('index')

def loginpage(request):
    return render(request,'loginpage.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,'logged in successfully')
            return redirect('companyregistration')
        else:
            return redirect('loginpage')
    else:
            return redirect('loginpage')
@login_required(login_url='loginpage')
def companyregistration(request):
    # x=User.objects.get(id=request.user.id)
    # var=company.objects.get(userid=x)
    return render(request,'companyregistration.html')

@login_required(login_url='loginpage')
def companysignup(request):
    try:
       
        if request.method=='POST':
            name=request.POST['name']
            companytype=request.POST['companytype']
            businessname=request.POST['businessname']
            email=request.POST['email']
            phone=request.POST['phone']
            website=request.POST['website']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pin=request.POST['pin']
            image=request.FILES['image']
            x=User.objects.get(id=request.user.id)

            if company.objects.filter(userid=x ).exists():
                return redirect('companyregistration')
            elif company.objects.filter(businessname=businessname).exists():
                return redirect('companyregistration')
            else:
                cmp=company(name=name,companytype=companytype,businessname=businessname,email=email,phone=phone,website=website,city=city,state=state,country=country,pin=pin,image=image,userid=x)
                cmp.save()
                
                return redirect('companypage')
        else:
            return redirect('companyregistration')
    except:
        return redirect('companyregistration')





@login_required(login_url='loginpage')
def companypage(request):
    x=User.objects.get(id=request.user.id)
    var=company.objects.get(userid=x)
    return render(request,'companypage.html',{'var':var})

def logout(request):
    auth.logout(request)
    messages.info(request,'logged out successfully')
    return redirect('loginpage')

