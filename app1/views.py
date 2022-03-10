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
    if request.session.has_key('brid'):
        brid = request.session['brid']
        var=branch.objects.filter(id=brid)
        return render(request,'empreg.html',{'var':var})


def employeereg(request):
    if request.session.has_key('brid'):
        brid = request.session['brid']
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
    if request.session.has_key('brid'):
        brid = request.session['brid']
        if request.session.has_key('brid'):
            brid = request.session['brid']

            empty=employee.objects.filter(branchid=brid)
            return render(request,'employeeshow.html',{'empty':empty})

def delete(request,id):
    if request.session.has_key('brid'):
        brid = request.session['brid']
        employees=employee.objects.get(id=id)
        employees.delete()
        return redirect('employeeshow')
def empedit(request,id):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        brid = request.session['brid']
        mem=employee.objects.get(id=id)
        var=branch.objects.filter(id=brid)
        return render(request,'empedit.html',{'mem':mem,'var':var})
    
def update(request,id):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        if request.method == 'POST':
            employees=employee.objects.get(id=id)
            employees.name=request.POST.get('name',employees.name)
            employees.email=request.POST.get('email',employees.email)
            employees.branchname=request.POST.get('branchname',employees.branchname)
            employees.password = request.POST.get('password',employees.password)
            employees.phone = request.POST.get('phone',employees.phone)
            employees.city = request.POST.get('city',employees.city)
            employees.state = request.POST.get('state',employees.state)
            employees.country = request.POST.get('country',employees.country)
            employees.pin = request.POST.get('pin',employees.pin)
            employees.image = request.FILES.get('image',employees.image)
           
            employees.save()
            return redirect('employeeshow')
        else:
            return redirect('empedit')
    

def logout(request):
    request.session['brid']=""
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        pass