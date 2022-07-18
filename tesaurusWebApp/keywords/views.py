from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from .tesaurus import Tesaurus

Tesaurus = Tesaurus()


def index(request):
    keywords = Tesaurus.getAllKeywords()
    return render(request, "keywords/index.html", {
        "keywords": keywords
    })


def keyword(request, keyword: str):
    # check keyword exists
    if not Tesaurus.keywordExists(keyword):
        # raise Http404()
        return HttpResponseNotFound("keyword doesn't exist")

    # return every piece of information associated
    keywordData = Tesaurus.getKeywordData(keyword)
    return render(request, 'keywords/single_keyword.html', {
        "keyword": keyword,
        "keywordData": keywordData,
    })

def getMatchKeywords(request, search:str):
    return HttpResponse('hola')
