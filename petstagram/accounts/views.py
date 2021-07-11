from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import UserProfileForm, LoginForm
from accounts.models import UserProfile
from pets.models import Pet


def login_view(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('landing')
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('landing')

def signup(request):
    user_form = UserCreationForm()
    profile_form = UserProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('landing')
            return redirect('login')
    return render(request, 'accounts/signup.html', context)



def profile_view(request, pk):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    pets = Pet.objects.filter(user=profile)
    profile_form = UserProfileForm(instance=profile)


    context = {
        'user': user,
        'profile': profile,
        'pets': pets,
        'profile_form': profile_form
    }
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile', profile.id)
    return render(request, 'accounts/user_profile.html', context)

