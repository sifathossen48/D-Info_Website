from django.contrib import admin

from Home_Page.models import FrequentlyQuestion, HeroSection, HowToCardWork, OrderStep, Products

# Register your models here.
class HeroSectionAdmin(admin.ModelAdmin):
  list_display = ('title', 'desc', 'image',)
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(OrderStep)
admin.site.register(HowToCardWork)
admin.site.register(FrequentlyQuestion)
admin.site.register(Products)
