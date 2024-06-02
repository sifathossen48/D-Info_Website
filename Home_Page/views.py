from django.shortcuts import render
from django.views.generic import TemplateView

from Home_Page.models import CardFeature, Feature, FrequentlyQuestion, HeroSection, HowToCardWork, OrderStep, Package, Products
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = HeroSection.objects.first()
        context['step'] = OrderStep.objects.all()
        context['howtowork'] = HowToCardWork.objects.all()
        context['fq'] = FrequentlyQuestion.objects.all()
        context['whiteMaterials'] = Products.objects.filter(is_white_material=True, is_draft=False, is_black_material=False,)
        context['blackMaterials'] = Products.objects.filter(is_black_material=True, is_draft=False, is_white_material=False,)
        context['packages'] = Package.objects.all()
        context['features'] = Feature.objects.all()
        context['up'] = CardFeature.objects.filter(is_up=True)
        context['down'] = CardFeature.objects.filter(is_down=True)
     
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'