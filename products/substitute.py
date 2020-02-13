from django.db.models import Q, Subquery, count

from .models import Product


def substitute(food_search):
    """ Propose a substitute for the search food """

    # food_substitute = Product.objects.filter(
    #     nutrition_group='a'
    # ).filter(
    #     categorie=food_search.categorie.id
    # )
    categories = food_search.categories.all()
    food_substitute = Product.objects.filter(
    ~Q(id=food_search.id),
    Q(categories_id__in=Subquery(categories.values("id"))),
    Q(nutrition_grade__lt=food_search.nutrition_grade),
    ).values("id", "name", "nutrition_grade", "url").annotate(count=Count("id"))



    if food_substitute:
        return food_substitute
    else:
        return None
