"""Contains function used for views app main."""
from django.shortcuts import render

from .forms import SearchForm


def result(request):
    """Display the site index."""
