from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  .models import CUser,Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache







# Create your views here.

@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invaild User name or password') 
    return render(request,'signin.html')
@never_cache
@login_required(login_url='signin')
def home(request):
    # messages.info(request,f"welcome {request.user.username}")
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'home.html',context) 

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect("signin")

def signup(request):
    if request.method == 'POST':
        email=request.POST['email']
        if  CUser.objects.filter(email=email).exists():
            messages.info(request,'you already have an accout')
        else:
            password1=request.POST['pas1']
            password2=request.POST['pas2']
            if password1 != password2:
                messages.info(request,'password are not same')
            elif not password2.isalnum():
                messages.info(request,'password must be alphanumeric')
            elif len(password2)<8:
                messages.info(request,'password must be 8 or more characters')
            else:
                CUser.objects.create(email=email,password=password2)
                return redirect('signin')          
    return render(request,'signup.html')

