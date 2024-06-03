from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Return_Policy(models.Model):
    description = RichTextField()
    arrive = RichTextField()
    