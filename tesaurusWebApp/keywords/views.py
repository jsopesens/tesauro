from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from rdflib import SKOS, Graph
from rdflib.namespace import RDF


def index(request):
    g = Graph()
    g.parse("3.owl")
    names = ""
    for subject, object in g.subject_objects(SKOS.prefLabel):
        names += "<li>"+object+"</li>"
    return HttpResponse("<lu>"+names+"</lu>")


def keywords(request, keyword):
    return HttpResponse(keyword)
