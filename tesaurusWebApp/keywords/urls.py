from django.urls import path
from . import views

# dynamic argument keyword on the URL to allow redirect to 
# every keyword page
# instead of redirecting one by one
urlpatterns = [
    path("", views.index),
    path("<str:keyword>", views.keyword, name="singular_keyword")
]