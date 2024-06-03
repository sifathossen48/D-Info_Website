from django.shortcuts import render
from django.views.generic import TemplateView

from TermsCondition.models import TermsAndCondition
# Create your views here.
class TermsView(TemplateView):
    template_name = 'termsCondition.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms'] = TermsAndCondition.objects.first()
        return context