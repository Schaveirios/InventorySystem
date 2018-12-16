from django.shortcuts import render, redirect
from user.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request,'login/login.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
@login_required
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photos' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['photos']
            profile.save()
            registered = True
            messages.success(request, 'Registered!')
        else:
            print(user_form.errors,profile_form.errors)
            messages.warning(request, 'Username already taken.')
            return render(request,'login/registration1.html',
                             {'registered':registered})
        return redirect('/warehouse/')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'login/registration1.html')
                    
                    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Login successful!')
                return redirect('/warehouse/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.warning(request, 'Wrong username or password.')
            return render(request, 'login/login.html', {})
    else:
        return render(request, 'login/login.html', {})