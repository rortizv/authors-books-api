from django.contrib import admin
from django.urls import path,include
from bookreview.views import AuthorView


urlpatterns = [
    path('books/', AuthorView.as_view())
]