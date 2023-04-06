from django.shortcuts import render, redirect
from . forms import UserRegisterForm, SignInForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


# Homepage view
def index(request):
    # make updates later
    return render(request,"shop/homepage.html")

"""
comment register 
"""
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.set_username(cd['username'])
            new_user.save()
            messages.success(request, "You're profile was sucessfully created")
            return redirect("shop:homepage")
    else:
        user_from = UserRegisterForm()
        return render(request, 'shop/register.html',{'user_form':user_form})
    

"""
comment signin
"""
def signin(request):
    if request.method == 'POST':
        user_signin = SignInForm(request.POST)
        if user_signin.is_valid():
            cd = user_signin.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
            else:
                messages.error(request,"Please check your credentials,either the username or password is incorrect ")
                return HttpResponse("Invalid username or password")
    else:
        user_signin(SignInForm)
        return render(request,'shop/signin.html',{'user_signin':user_signin})

"""
comment signout
"""
def signout(request):
    logout(request)
    messages.success(request,"You've been sucessfully signout")
    return redirect("shop:signin")

