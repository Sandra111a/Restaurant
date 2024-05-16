from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from forms import LoginForm, RegistrationForm


class LoginView(View):
    """Widok zawiera formularz logowania użytkownika.
    Wymaga nazwy użytkownika - username i hasła - password1.
    """
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form,
        }
        return render(request, 'login.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'],
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, 'Zostałeś zalogowany')
                return redirect('home')
        messages.error(request, 'Nieprawidłowy login lub hasło')
        return render(request, 'login.html', {'form': form})


class RegistrationView(View):
    """Widok zawiera formularz rejestracji nowego użytkownika.
    Wymaga podania loginu, hasła oraz adresu e-mail.
    """

    def get(self, request):
        form = RegistrationForm()
        ctx = {
            'form': form,
        }
        return render(request, 'registration.html', ctx)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.login = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration.html', {'form': form})


