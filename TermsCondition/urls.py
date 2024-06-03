from django.urls import path

from . import views


urlpatterns = [
    path('', views.TermsView.as_view(), name='terms'),
]