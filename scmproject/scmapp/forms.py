from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'profile_pic']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "name",
        "type": "text",
        "placeholder": "Username"
    }), label="Username")
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "text-name",
        "type": "email",
        "placeholder": "Email"
    }), label="Email")
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "text-name",
        "type": "password",
        "placeholder": "Password"
    }), label="Password")
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "text-name",
        "type": "password",
        "placeholder": "Confirm Password"
    }), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
