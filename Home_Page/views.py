from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from Home_Page import forms
from Home_Page.models import CardFeature, Feature, FrequentlyQuestion, HeroSection, HowToCardWork, OrderStep, Package, Products, Review
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
        context['reviews'] = Review.objects.all()
     
        return context

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully') # Redirect to a success page
        else:
            # Print form errors to console for debugging
            print(form.errors)
            messages.error(request, 'Invalid! Please try again.')
    else:
        form = forms.ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

class AllPackView(TemplateView):
    template_name = 'all-package.html'