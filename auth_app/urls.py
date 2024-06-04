from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login')
]