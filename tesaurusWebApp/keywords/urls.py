from django.urls import path
from . import views

# dynamic argument keyword on the URL to allow redirect to 
# every keyword page
# instead of redirecting one by one
urlpatterns = [
    path("", views.index, name="index"),
    path("getMatchKeywords/<str:search>", views.getMatchKeywords, name="getMatchKeywords"),
    path("getSonsOf/<str:keyword>", views.getSonsOf, name="getSonsOf"),
    path("<str:keyword>", views.keyword, name="singular_keyword"),
]