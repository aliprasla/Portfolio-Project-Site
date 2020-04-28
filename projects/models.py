from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=750)
    short_description = models.TextField(default="")
    long_description = models.TextField(default="")
    last_modified_on = models.DateTimeField(auto_now=True)
    url = models.URLField(default="")


