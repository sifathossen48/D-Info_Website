from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from auth_app import forms
from . forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView


# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'registration.html')
#     def post(self, request):
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             password = form.data['password']
#             user = form.save()
#             user.set_password(password)
#             user.save()
#             messages.success(request, 'Registration successfully done')
#             return redirect('/auth/login/')

#         else:
#             messages.error(request, 'Invalid data')
#         context = {form: 'form'}
#         return render(request, 'registration.html', context=context)
class PasswordReset(View):
    def get(self,request):
        return render(request, 'password-forgot.html')
    def post(self,request):
        return render(request, 'password-forgot.html')
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            password = form.data['password']
            user = form.save()
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successfully done')
            return render(request, 'login.html')

        else:
            messages.error(request, 'Invalid data')

        context = {form: 'form'}
        return render(request, 'registration.html', context=context)

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            password = form.data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('/')
                messages.error(request, 'Password did not match')
            except ObjectDoesNotExist:
                messages.error(request, 'User not found')
        else:
            messages.error(request, 'Invalid data')
        context = {'form': form}
        return render(request, 'login.html', context=context)
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'password-forgot.html'