from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.validators import MinLengthValidator

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(), validators=[MinLengthValidator(6)])
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
    
    
        
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=32)



class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is not registered. Please register first.")
        return email
