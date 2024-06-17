from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

from django import forms
from .models import ImageResult







class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']





class ImageUploadForm(forms.ModelForm):
    cancer_type = forms.ChoiceField(choices=[('Brain', 'Brain'), ('Breast', 'Breast'), ('Kidney', 'Kidney')])

    class Meta:
        model = ImageResult
        fields = ['image', 'cancer_type']

