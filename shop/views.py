from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserRegisterForm, SignInForm, ProfileEditForm, UserEditForm
from . models import Profile
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# TODO: create the index function
def index(request):
    """
      The function takes a request and return the render for the index page. 
    """
    # make updates later
    return render(request,"shop/index.html")


# TODO: Create the Home view
def home(request):
    """
      The function takes a request and return the render for the home page. 
    """
    # make updates later
    return render(request,"shop/homepage.html")

# TODO: Create the user registration view
def register(request):
    """
    Processes the annonymous user request too register an account
    param: request 
    function: if the form request is post, 
                Process a new userRegistration form object with user data.
                Next checks for form validation and sets the new users password and username.
                next display success message, and redirects too users homepage. 
            else
                create a new userRegistration form object and return render. 
    """
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.set_username(cd['username'])
            new_user.save()
            messages.success(request, "You're profile was sucessfully created")
            return redirect("shop:signin")
    else:
        user_form = UserRegisterForm()
        context = {
            'user_form':user_form,
        }
        return render(request, 'shop/register.html',context)
    
# TODO: Create user login view
def signin(request):
    """
    Processes the annonymous user request too login
    param: request 
    function: if the form request is post, 
                Process a new usersigin form object with user data.
                Next checks for form validation and authenticate the cleaned data against the database.
                if the user exist, login the user and redirect to home page
            else
                create a new Signin form object and return render. 
    """
    if request.method == 'POST':
        user_signin = SignInForm(request.POST)
        if user_signin.is_valid():
            cd = user_signin.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'Sucessfully logged in')
                return redirect("shop:homepage")
            else:
                messages.error(request,"Please check your credentials,either the username or password is incorrect ")
                return HttpResponse("Invalid username or password")
    else:
        user_signin = SignInForm()
        return render(request,'shop/signin.html',{'user_signin':user_signin})

# TODO: create user signout view
def signout(request):
    """
    Logout the authenticated user
    param: request 
    function: Processes the users request to logout, displays message
    returns: redirect to index page 
    """
    logout(request)
    messages.success(request,"You've been sucessfully signout")
    return redirect("shop:index")


# TODO: Create user profile page
def profile_page(request,id):
    """
    Gets current users profile
    param: request, user.id
    function: attempts to retrieve an indiviual Profile Object associted with the users ID or returns a 404 error
    returns: template render and profile object
    """
    user_profile = get_object_or_404(Profile, id=id)
    context = {
        'user_profile':user_profile,
    }
    return render(request,"shop/profile.html",context)

@login_required
def account_edit(request):
    if request.method == 'POST':
        user_edit = UserEditForm(request.POST, instance=request.user)
        profile_edit = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_edit.is_valid and profile_edit.is_valid:
            user_edit.save()
            profile_edit.save()
            messages.success(request, "You're profile was sucessfully updated")
            return redirect('shop:homepage')
    else:
        user_edit = UserEditForm(instance=request.user)
        profile_edit = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_edit':user_edit,
            'profile_edit': profile_edit
        }
        return render(request,"shop/edit_account.html",context)