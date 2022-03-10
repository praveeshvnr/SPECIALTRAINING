from django.shortcuts import render,redirect
from django.contrib import messages

from app.models import *
from .models import *


# Create your views here.
def branchreg(request):
    
    var=company.objects.all()
    return render(request,'branchreg.html',{'var':var})
def branchsignup(request):
    try:
        if request.method=="POST":
            branchname=request.POST['branchname']
            businessname=request.POST['businessname']
            email=request.POST['email']
            password=request.POST['password']
            phone=request.POST['phone']
            website=request.POST['website']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pin=request.POST['pin']
            image=request.FILES['image']
            x=company.objects.get(businessname=businessname)

            if branch.objects.filter(branchname=branchname).exists():
                return redirect('branchreg')
            else:
                cmp=branch(branchname=branchname,businessname=businessname,email=email,password=password,phone=phone,website=website,city=city,state=state,country=country,pin=pin,image=image,companyid=x)
                cmp.save()
                return redirect('branchlog')
        else:
            return redirect('branchreg')
    except:
       return redirect('branchreg')

def branchlog(request):
    return render(request,'branchlog.html')

def branchlogin(request):
    if request.method=='POST':
        if branch.objects.filter(branchname=request.POST['branchname'],password=request.POST['password']).exists():
            member=branch.objects.get(branchname=request.POST['branchname'], password=request.POST['password'])
            request.session['brid'] = member.id
        
            return redirect('empreg')
        else:
            return redirect('branchlog')

    else:
        return redirect('branchlog')

def empreg(request):
    return render(request,'empreg.html')