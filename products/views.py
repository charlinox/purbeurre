"""Contains function used for views app search."""
from django.shortcuts import render

from .forms import search


def index(request):
    """Display the site index."""
    return render(request, 'search/index.html', {'form': search()})

