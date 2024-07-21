from typing import Any
from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'access_level', 'username']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password("12345678")
        if commit:
            user.save()
        return user


class CreateCollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['title']


class CreateTermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['title']

