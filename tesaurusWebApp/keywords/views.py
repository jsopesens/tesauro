from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound




def index(request):
    return HttpResponse("aqui se leera el doc owl con Owlready")
    


def keywords(request, keyword):
    return HttpResponse(keyword)