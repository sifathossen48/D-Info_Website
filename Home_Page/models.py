from django.db import models

# Create your models here.
class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    favicon = models.ImageField(upload_to='favicon/')
    card_setup_video = models.CharField(max_length=200)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=100)
    google_map_link = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    def __str__(self):
        return self.site_name
      
class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='heroSection/')

class OrderStep(models.Model):
    step_number = models.IntegerField()
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=250)
    def __str__(self):
        return self.title
    
class HowToCardWork(models.Model):
    title = models.CharField(max_length=30)
    icon = models.FileField(upload_to='icon/')
    desc = models.TextField(max_length=200)
    def __str__(self):
        return self.title
    
class FrequentlyQuestion(models.Model):
    question = models.CharField(max_length=80)
    answer = models.TextField()
    def __str__(self):
        return self.question
    
class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image_1 = models.ImageField(upload_to='products/' )
    image_2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='products/', null=True, blank=True)
    is_black_material = models.BooleanField(default=False)
    is_white_material = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name
  
class Feature(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
class CardFeature(models.Model):
    title = models.CharField(max_length=50)
    is_up = models.BooleanField(default=True)
    is_down = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Partner(models.Model):
    companyName = models.CharField(max_length=30)
    companyLogo = models.ImageField(upload_to='partner/')
    def __str__(self):
        return self.companyName
class Review(models.Model):
    client = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='client')
    profile_link = models.CharField(max_length=80)
    message = models.TextField()
    def __str__(self):
        return self.client
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=40)
    message = models.TextField()
    def __str__(self):
        return self.name