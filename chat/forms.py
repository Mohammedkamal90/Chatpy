from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Group


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={'class': 'block-inline mb-2 mr-20 ml-3 px-4 py-2 rounded border border-gray-300 placeholder-gray-500', 'placeholder': 'Username'}),
        'password1': forms.PasswordInput(attrs={'class': 'block-inline mb-2 mr-25 ml-3 px-4 py-2 rounded border border-gray-300 placeholder-gray-500', 'placeholder': 'Password'}),
        'password2': forms.PasswordInput(attrs={'class': 'block mb-4 ml-5 mr-20 px-4 py-2 rounded border border-gray-300 placeholder-gray-500', 'placeholder': 'Confirm Password', }),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md'
            }),
        }

