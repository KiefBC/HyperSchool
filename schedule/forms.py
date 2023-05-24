from django import forms
from django.forms import ModelForm
from .models import Student


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100, required=False)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
