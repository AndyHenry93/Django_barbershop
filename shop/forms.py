from django import forms
from django.contrib.auth.models import User
from . models import Profile


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label="Confirm Password")
    birthdate = forms.DateField(input_formats='%m/%d/%Y',label="Date of birth ('mm/dd/yyyy)")
    is_barber = forms.BooleanField(required=True,label="Are you a barber?")


    class Meta:
        model = User
        fields = ['first_name','last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("you're passwords didn't match, please double check your credentials")
        

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar','bio']


class UserEditForm(forms.ModelForm):
     username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
     email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
     
     class Meta:
        model = User
        fields = ['username','email']

