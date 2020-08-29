from django import forms

from account.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'fadeIn second', 'id': 'login', 'placeholder': 'login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'fadeIn third', 'id': 'password', 'placeholder': 'password'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class TestForm(forms.Form):
    name = forms.CharField()
