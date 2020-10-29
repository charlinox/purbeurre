from django.db.models import Q, Subquery, Count

from .models import Product


def substitute(food_search):
    """ Propose a substitute for the search food """

    search_categories = food_search.categories.all()

    food_substitute = Product.objects.filter(
        ~Q(id=food_search.id),
        Q(categories__id__in=Subquery(food_search.categories.all().values('id'))),
        Q(nutrition_grade__lt=food_search.nutrition_grade)
    ).values("id", "name", "nutrition_grade", "url", "image_url").annotate(count=Count('id')).order_by("-count")

    return food_substitute
