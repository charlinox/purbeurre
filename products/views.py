"""Contains function used for views app main."""
from django.shortcuts import render
from django.views import generic

from .forms import SearchForm
from .models import Product


def result(request):
    """Display the site index."""

    context = {}

    if request.method == 'POST':

        form = SearchForm(request.POST)
        if form.is_valid():
            food_search = form.cleaned_data['research']
            food = Product.objects.filter(name__contains=food_search)

            if food.exists():
                sub = substitute(food[0])
                context['match'] = True
                context['food'] = food[0]
                context['list_food'] = sub
            
            else:
                context['match'] = False
        
        else:
            context['errors'] = form.errors.items()

        return render(request, 'search/result.html', context=context)
    
    else:
        return render(request, 'search/no_search.html', context=context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/food_detail.html'
