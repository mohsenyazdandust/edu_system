from typing import Any
from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'access_level', 'username', 'cgroup', 'college']
        
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


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'short']


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code',]


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']


class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title']


class CreateTimingForm(forms.ModelForm):
    class Meta:
        model = Timing
        fields = ['title']


class CreateLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['title']