from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('allpackage/', views.AllPackView.as_view(), name='allpack')
]