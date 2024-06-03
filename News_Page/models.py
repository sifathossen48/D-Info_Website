from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image_1 = models.ImageField(upload_to='news/')
    image_2 = models.ImageField(upload_to='news/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='news/', blank=True, null=True)
    def __str__(self):
        return self.title