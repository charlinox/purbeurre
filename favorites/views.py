from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Favorite
from products.models import Product

@login_required
def save_food(request):
    if request.method=="POST"
        food_id = request.POST["food_id"]
        substitute_id = request.POST["substitute_id"]
        req = request.POST['idFood']
        fav = Favoris()
        fav.user = request.user
        fav.substitute = Product.objects.get(pk=req)
        fav.save()

    return JsonResponse({'ServerResponse': 'okay'})

@login_required
def my_food(request):
    context = {}
    if request.user.is_authenticated:
        food_favs = Favorite.objects.filter(user=request.user.id)
        context['list_food'] = food_favs

    return render(request, 'favorites/my_food.html', context=context)
