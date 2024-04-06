from django.shortcuts import render
from django.views.generic import TemplateView

# Qachonki classga murojaat qilinganda, bu classdagi 'template_name' nomli o'zgaruvchi 'home.html' fayliga murojaat qiladi.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'
# Create your views here.
