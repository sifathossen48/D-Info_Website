
from django.shortcuts import render
from django.views.generic import TemplateView

from News_Page.models import News


# Create your views here.
class NewsView(TemplateView):
    template_name = 'newsroom.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context
