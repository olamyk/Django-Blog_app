from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.

class IndexTemplate(TemplateView):
    template_name = 'myApp/index.html'

class BlogTemplate(TemplateView):
    template_name = 'myApp/blog.html'

class SIngleTemplate(TemplateView):
    template_name = 'myApp/single.html'

class LoginTemplate(TemplateView):
    template_name = 'myApp/login.html'
