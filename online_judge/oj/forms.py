from django import forms
from django.contrib.auth.models import User
# from .models import

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
# class LoginForm(forms.ModelForm):
#     pass

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()
