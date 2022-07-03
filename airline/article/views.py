from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.
def article_detail(request, slug):
    return HttpResponse(slug)