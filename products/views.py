"""Contains function used for views app search."""
from django.shortcuts import render

from .forms import SearchForm


def index(request):
    """Display the site index."""
    return render(request, "search/index.html", {"form": SearchForm()})


def result(request):
    """Display the site index."""
    return render(request, "search/index.html", {"form": SearchForm()})
