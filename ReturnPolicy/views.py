
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Return_Policy

# Create your views here.
class PolicyView(TemplateView):
    template_name = 'returnPolicy.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['policy'] = Return_Policy.objects.all()
        return context