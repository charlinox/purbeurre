from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .forms import ConnexionForm

def signup(request):

    if request.user.is_authenticated:
         return redirect('index')         
    else:

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')

        else:
            form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form}) 

def account(request):
    context = {}

    if request.user.is_authenticated:
        context['pseudo'] = request.username

    else:
        return redirect(reverse('users:login'))

    return render(request, 'users/account.html', context=context)
