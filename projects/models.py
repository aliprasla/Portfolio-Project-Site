from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_description = models.TextField()
    last_modified_on = models.DateTimeField(auto_now=True)