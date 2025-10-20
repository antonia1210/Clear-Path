from django import forms
from django.contrib.auth.forms import UserCreationForm

from churches.models import Church
from .models import User

class SignupForm(UserCreationForm):
    full_name = forms.CharField(required=True, label='Nume și prenume')
    email = forms.EmailField(required=True, label='Email')
    assigned_church = forms.ModelChoiceField(
        queryset=Church.objects.all(),
        required=True,
        label='Parohie'
    )
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'assigned_church', 'password1', 'password2')
        labels = {
            'username':'Nume utilizator',
            'assigned_church':'Parohie',
            'password1':'Parolă',
            'password2':'Confirmare parolă',
        }