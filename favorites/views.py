import json

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Favorite
from products.models import Product

@login_required
def save_food(request):
    if request.is_ajax and request.method=="POST":
        substitute_id=request.POST["substitute-id"]
        product_id=request.POST["product-id"]
        substitute= Product.objects.get(pk=substitute_id)
        product= Product.objects.get(pk=product_id)
        Favorite.objects.create(substitut=substitute, original=product, user=request.user)

    return JsonResponse({'ServerResponse': 'okay'})

@login_required
def my_food(request):
    context = {}
    food_favs = Favorite.objects.filter(user=request.user.id)
    context['list_food'] = food_favs

    return render(request, 'favorites/my_food.html', context=context)
