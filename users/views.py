from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import ConnexionForm


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'users/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))    

# def signup(request):
#     error = False

#     if request.method == "POST":
#         form = ConnexionForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#             else:
#                 error = True
#     else:
#         form = ConnexionForm()

#     return render(request, 'users/connexion.html', locals())


def signup(request):

    if request.user.is_authenticated():
         return redirect('dashboard')
    else:

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data.get('username')
                last_name = form.cleaned_data.get('usersurname')
                aka = form.cleaned_data.get('useraka')
                user_email = form.cleaned_data.get('useremail')
                user_password = form.cleaned_data.get('userpassword')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('dashboard')

        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form}) 
