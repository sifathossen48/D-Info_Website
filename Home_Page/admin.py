from django.contrib import admin

from Home_Page.models import CardFeature, Feature, FrequentlyQuestion, HeroSection, HowToCardWork, OrderStep, Package, Partner, Products, Review

# Register your models here.
class HeroSectionAdmin(admin.ModelAdmin):
  list_display = ('title', 'desc', 'image',)
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(OrderStep)
admin.site.register(HowToCardWork)
admin.site.register(FrequentlyQuestion)
admin.site.register(Products)
admin.site.register(Package)
admin.site.register(Feature)
admin.site.register(CardFeature)
admin.site.register(Partner)
admin.site.register(Review)