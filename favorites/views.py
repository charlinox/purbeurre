from django.shortcuts import render

def savefood(request):
    req = request.POST['idFood']
    fav = Favoris()
    fav.user = request.user
    fav.substitute = Products.objects.get(pk=req)
    fav.save()

    return JsonResponse({'ServerResponse': 'okay'})

def myfood(request):
    context = {}
    if request.user.is_authenticated:
        food_save = Favorites.objects.filter(user=request.user.id)
        context['list_food'] = food_save

    return render(request, 'my_food.html', context=context)
