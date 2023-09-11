from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ReferralCode
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request,'index.html')

def refral(request):
    return render (request,'refral.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.success(request, 'Username is already exists!')
            return render(request, 'register.html')
        elif User.objects.filter(email=email).exists():
            messages.success(request, 'Email is already exists !')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=username, password=password)
            referral_code = ReferralCode(user=user)
            referral_code.save()
            messages.success(request, 'Account created successfully!')
            return redirect('ulogin')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'ulogin.html')

@login_required
def dashboard(request):
    codes=ReferralCode.objects.filter(user=request.user)
    return render(request, 'dashboard.html',{'codes':codes})

def register_with_referral(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        refer = request.POST['referrer']
        if User.objects.filter(username=username).exists():
            messages.success(request, 'Username is already exists!')
            return render(request, 'refral.html')
        else:
            user = User.objects.create_user(username=username, password=password)
            referrer = ReferralCode.objects.get(code=refer).user
            referral_code = ReferralCode(user=user, referred_by=referrer)
            referral_code.save()
            messages.success(request, 'Account created successfully with referral!')
            return redirect('ulogin')
    else:
        messages.info(request,'Incorrect Referral Code')
        return render(request, 'refral.html')
