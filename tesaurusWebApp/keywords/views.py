from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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
        return HttpResponseNotFound("keyword doesn't exist")

    # return every piece of information associated
    keywordData = Tesaurus.getKeywordData(keyword)
    return render(request, 'keywords/single_keyword copy.html', {
        "keyword": keyword,
        "keywordData": keywordData,
    })
