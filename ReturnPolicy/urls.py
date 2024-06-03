from django.urls import path

from . import views


urlpatterns = [
    path('', views.PolicyView.as_view(), name='policy'),

]