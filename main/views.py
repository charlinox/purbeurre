from django.shortcuts import render

from products.forms import SearchForm


def index(request):
    """Display the site index."""
    return render(request, "main/index.html", {"form": SearchForm()})
