from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

from rdflib import SKOS, Graph
from rdflib.namespace import RDF


def index(request):
    g = Graph()
    g.parse("3.owl")
    keywords = []
    for object in g.objects(None, SKOS.prefLabel):
        keywords.append(object)
    return render(request, "keywords/index.html",{
        "keywords": keywords
    })


def keywords(request, keyword):
    return HttpResponse(keyword)
