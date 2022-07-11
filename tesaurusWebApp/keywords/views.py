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


def keywords(request, keyword: str):
    # check keyword exists
    if not Tesaurus.keyword_exists(keyword):
        return HttpResponseNotFound("keyword doesn't exist")

    # return every piece of information associated
    keyword_data= Tesaurus.get_data(keyword)
    return render(request, 'keywords/single_keyword.html', {
        "keyword": keyword,
        "keyword_data": keyword_data,
    })
