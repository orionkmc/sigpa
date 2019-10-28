from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login as users_login, \
    logout as users_logout
from user.forms import LoginForm
from user.models import Profile


# Login User
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni')
            password = form.cleaned_data.get('password')
            try:
                username = Profile.objects.get(dni=dni).user.username
            except Profile.DoesNotExist:
                username = None
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    users_login(request, user)
                    return redirect(request.GET.get('next', 'home'))
            else:
                error_messages.append('Error de Usuario y/o Contraseña')
        context = {
            'errors': error_messages,
            'form': form
        }
        return render(request, 'login.html', context)


# Logout User
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            users_logout(request)
        return redirect('user:login')
