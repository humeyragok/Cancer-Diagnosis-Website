from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile





class userRegisterForm(UserCreationForm):
    email = forms.EmailField(label="E-posta")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Kullanıcı Adı',
            'password1': 'Şifre',
            'password2': 'Şifre Tekrarı',
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']



