from django.db import models


class Project(models.Model):
    project_name = models.CharField()
    project_description = models.CharField()