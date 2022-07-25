from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse

from .tesaurus import Tesaurus

Tesaurus = Tesaurus()

# aquesta funció ha de canviar per a millorar la ordenació dels elements en format arbre... ademés pot allegerir la carrega en temps
# def index(request):
#     keywords = Tesaurus.getAllKeywords()
#     return render(request, "keywords/index.html", {
#         "keywords": keywords
#     })
def index(request):
    keywords = Tesaurus.getTopConcepts()
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


def getMatchKeywords(request, search: str):
    # get search parameter and search every NamedIndividual that contains that string
    keywords = Tesaurus.getKeywordsMatching(search)
    return JsonResponse({'keywords': keywords})


def getSonsOf(request, keyword: str) -> JsonResponse:
    keywordData = Tesaurus.getKeywordData(keyword)
    return JsonResponse({'topConcepts': keywordData['hasTopConcept']})