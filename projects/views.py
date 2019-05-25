from django.shortcuts import render
from django.http import HttpResponse

dummy_data = [
    {
        'name':'MNIST',
        'description':'MNIST application'
    },
    {
        'name':"Classifier Viz",
        'description':"Some cool classifier visualization"
    }
]
def home(request):
    context = {
        'projects':dummy_data
    }
    return render(request,'projects/home.html',context)

def about(request):
    return render(request,'projects/about.html')