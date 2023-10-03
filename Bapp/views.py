from django.shortcuts import render,redirect
from .forms import Doner_registration,Buser_registration
from .models import Doner,Buser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import AuthenticationForm
 
# Create your views here.


def index(request):
    return render(request,'index.html')

def doner_reg(request):
    if request.method=='POST':
        form = Doner_registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            dname = form.cleaned_data.get('Doner_name')
            dplace = form.cleaned_data.get('Doner_place')
            daddress = form.cleaned_data.get('Doner_address')
            dbloodtype = form.cleaned_data.get('Doner_blood_type')
            dcontactnumber = form.cleaned_data.get('Doner_contact_number')
            user = User.objects.get(username = username)
            ddata = Doner.objects.create(user=user,Doner_name=dname,
                                         Doner_place=dplace,Doner_address=daddress,
                                         Doner_blood_type=dbloodtype,
                                         Doner_contact_number=dcontactnumber)           
            ddata.save()
            return redirect('/')
    form =Doner_registration()
    context = {'form':form}
    return render(request,'doner_reg.html',context)



def buser_reg(request):
    if request.method=='POST':
        form = Buser_registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            buname = form.cleaned_data.get('Buser_name')
            buplace = form.cleaned_data.get('Buser_place')
            buaddress = form.cleaned_data.get('Buser_address')
            bubloodtype = form.cleaned_data.get('Buser_blood_type')
            bucontactnumber = form.cleaned_data.get('Buser_contact_number')
            user = User.objects.get(username = username)
            ddata = Buser.objects.create(user=user,Buser_name=buname,
                                         Buser_place=buplace,Buser_address=buaddress,
                                         Buser_blood_type=bubloodtype,
                                         Buser_contact_number=bucontactnumber)           
            ddata.save()
            return redirect('/')
    form =Buser_registration()
    context = {'form':form}
    return render(request,'buser_reg.html',context)



def admin_log(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')        
            user = authenticate(username=username,password=password)
            if user is not None and user.is_staff==True:
                login(request,user)
                return redirect('/admin_page')
            else:
                return redirect('/admin_log')
        else:
            return redirect('/admin_log')
    else:

        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'admin_log.html',context)



def admin_page(request):
    buser = Buser.objects.all()
    doner = Doner.objects.all()
    user = User.objects.all()
    context = {'buser':buser,'doner':doner,'user':user}
    return render(request,'admin_page.html',context)


def dele(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/admin_page')


def log_out(request):
    logout(request)
    return redirect('/')