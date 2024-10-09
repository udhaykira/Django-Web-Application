from django import forms
from django.contrib.auth.models import User
#here user is a django predefined user who have username and all
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=['username','email','password1','password2']

