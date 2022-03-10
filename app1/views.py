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
    var=branch.objects.all()
    return render(request,'empreg.html',{'var':var})


def employeereg(request):
    try:
        if request.method =='POST':
            name=request.POST['name']
            email=request.POST['email']
            branchname=request.POST['branchname']

            password=request.POST['password']
            phone=request.POST['phone']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pin=request.POST['pin']
            image=request.FILES['image']

            x=branch.objects.get(branchname=branchname)

            if employee.objects.filter(name=name).exists():
                return redirect('empreg')

            else:
                emp=employee(name=name,email=email,branchname=branchname,password=password,phone=phone,city=city,state=state,country=country,pin=pin,image=image,branchid=x)
                emp.save()
                return redirect('employeeshow')
        else:
            return redirect('empreg')
    except:
        return redirect('empreg')

def employeeshow(request):
    empty=employee.objects.all()
    return render(request,'employeeshow.html',{'empty':empty})

def delete(request,id):
    employees=employee.objects.get(id=id)
    employees.delete()
    return redirect('employeeshow')
def empedit(request,id):
    return render(request,'empedit.html')