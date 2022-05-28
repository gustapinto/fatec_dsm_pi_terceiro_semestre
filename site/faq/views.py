from django.views.generic import TemplateView
from django.shortcuts import render,  redirect

from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
class FaqView(TemplateView):
    template_name = "faq.html"
    
