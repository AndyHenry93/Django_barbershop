from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserRegisterForm, SignInForm, ProfileEditForm, UserEditForm, BarberEditForm
from . models import Profile
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# login helper function
def login_user(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
    else:
        messages.error(request,"Please check your credentials,either the username or password is incorrect ")
        return HttpResponse("Invalid username or password")

# TODO: create the index function
def index(request):
    """
      The function takes a request and return the render for the index page. 
    """
    # make updates later
    return render(request,"shop/index.html")

# TODO: Create the Home view
@login_required
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
            new_user.username = cd['username']
            new_user.save()
            # login the user
            login_user(request,cd['username'],cd['password'])
            messages.success(request, "You're profile was sucessfully created, Please upload your profile image")
            return redirect("shop:edit")
    else:
        user_form = UserRegisterForm()
        return render(request, 'shop/register.html',{'user_form':user_form})
    
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
            login_user(request,cd['username'],cd['password'])
            return redirect("shop:homepage")
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

# TODO:
@login_required
def account_edit(request):
    if request.method == 'POST':
        user_edit = UserEditForm(request.POST, instance=request.user)
        profile_edit = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_edit.is_valid and profile_edit.is_valid:
            user_edit.save()
            profile_edit.save()
            if request.user.profile.is_barber:
                return redirect('shop:barber_edit')
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

# TODO: 
@login_required
def barber_edit(request):
    if request.method == 'POST':
        barber_form = BarberEditForm(request.POST)
        if barber_form.is_valid():
            barber_form.save()
            messages.success(request, "You're profile was sucessfully updated")
        return redirect('shop:homepage')
    else:
        barber_form = BarberEditForm()
        return render(request,"shop/barber_edit.html",{'barber_form':barber_form})