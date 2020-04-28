"""
Url routing for projects app
"""

from django.urls import path,re_path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.home,name='home'),
    path('about', views.about, name='about'),
    path('index_js',views.index_js,name='index_js'),
    re_path(r'^projects/(.*)',views.generic_project_view,name='project_view')
]



