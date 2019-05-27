from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    context = {
        'projects':models.Project.objects.all()
    }
    return render(request,'projects/home.html',context)

def about(request):
    return render(request,'projects/about.html')