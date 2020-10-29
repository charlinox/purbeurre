"""Contains function used for views app main."""
from django.shortcuts import render
from django.views import generic

from .forms import SearchForm
from .models import Product
from .substitute import substitute


def result(request):
    """Display the product substitutes"""

    context = {}

    form = SearchForm(request.GET)
    if form.is_valid():
        food_search = form.cleaned_data['research']
        food = Product.objects.filter(name__contains=food_search)

        if food.exists():

            sub = substitute(food[0])[:9]
            context['match'] = True
            context['food'] = food[0]
            context['list_food'] = sub

        else:
            context['match'] = False
            return render(request, 'products/no_search.html')
    else:
        context['errors'] = form.errors.items()

    return render(request, 'products/result.html', context=context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/food_detail.html'
