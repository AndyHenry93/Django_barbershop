from django import forms
from django.contrib.auth.models import User

"""
comments for register
"""
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label="Confirm Password")
    birthdate = forms.DateField(input_formats='%m/%d/%Y')

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("you're passwords didn't match, please double check your credentials")
        

"""
Comments for Sign in 
"""
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)