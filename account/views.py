from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from .forms import UserLoginForm, ProfileForm, TestForm


@login_required
def user_profile(request):
    Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html')


@login_required
def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'accounts/create_profile.html', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)


@login_required
def dashboard(request):

    return render(request, 'accounts/dashboard.html')


def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            context = {
                'form': form,
                'error': "Invalid username or password !!"
            }
            return render(request, 'accounts/login.html', context)

    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')