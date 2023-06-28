from django import forms
from django.contrib.auth.models import User
from . models import Profile


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label="Confirm Password")

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

class UserEditForm(forms.ModelForm):
     username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
     email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
     
     class Meta:
        model = User
        fields = ['username','email']

class ProfileEditForm(forms.ModelForm):
    avatar = forms.ImageField(label="Profile Image",widget=forms.FileInput(attrs={'class': 'form-control-file'}),required=False)
    is_barber = forms.BooleanField(label="Are you a barber?",required=False)

    class Meta:
        model = Profile
        fields = ['avatar','is_barber']

class BarberEditForm(forms.ModelForm):
    bio = forms.CharField(max_length=500, required=True, label = "Bio", widget=forms.TextInput(attrs={'placeholder': 'Describe yourself...'}))
    shop_name = forms.CharField(max_length=100, required=True, label = "Shop Name")
    shop_address = forms.CharField(max_length=100, required=True, label = "Shop Address")
    client_photo = forms.ImageField(label="Client photos",required=False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['bio','shop_address','shop_name','client_photo']