from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class TermsAndCondition(models.Model):
    title = models.CharField(max_length=30)
    last_Updated = models.DateField(auto_now=True)
    interpretation = models.TextField()
    definitions = RichTextField()
    acknowledgment = RichTextField()
    others = RichTextField()
    def __str__(self):
        return self.title