from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from About_Page.models import WhyChooseUs


# Create your views here.
class HomeView(TemplateView):
    template_name = 'aboutus.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choose'] = WhyChooseUs.objects.all()
     
        return context