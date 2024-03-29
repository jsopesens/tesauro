from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse

from .tesaurus import Tesaurus

Tesaurus = Tesaurus()

def index(request):
    keywords =  Tesaurus.getConceptSchemes()
    return render(request, "keywords/index.html", {
        "keywords": keywords
    })


def keyword(request, keyword: str):
    # check keyword exists
    if not Tesaurus.keywordExists(keyword):
        return HttpResponseNotFound("keyword doesn't exist")
        # raise Http404()

    # return every piece of information associated
    keywordData = Tesaurus.getKeywordData(keyword)
    return render(request, 'keywords/single_keyword.html', {
        "keyword": keyword,
        "keywordData": keywordData,
    })


def getMatchKeywords(request, search: str):
    # get search parameter and search every NamedIndividual that contains that string
    keywords = Tesaurus.getKeywordsMatching(search)
    return JsonResponse({'keywords': keywords})


def getChildrenOf(request, keyword: str) -> JsonResponse:
    # get the children of the current element
    children = Tesaurus.getChildrenOf(keyword)
    
    # generate dictionary with the keywords and a boolean value that indicates if that keyword had more children
    result = {}
    for child in children:
        result[child] = 1 if (Tesaurus.checkKeywordNarrower(child) or Tesaurus.checkKeywordTopConcept(child)) else 0
    
    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return JsonResponse({'children': result})
