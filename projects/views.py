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

def generic_project_view(request,*kwargs):
    # get project

    request.path += '/index.html'
    
    #NOTE: all core projects require an index.html file
    return render(request,request.path)

def index_js(request):
    return render(request,'projects/static/index.js')