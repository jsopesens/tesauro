from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def keywords(request, keyword):
    return HttpResponse(keyword)