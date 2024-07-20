from django.shortcuts import render
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html', {'title': 'Register'})


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html', {'title': 'Login'})


class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/reset-password.html', {'title': 'Reset Password'})


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/forgot-password.html', {'title': 'Forgot Password'})