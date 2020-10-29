from django.test import TestCase, Client
from ..models import Category, Product
from ..views import result, DetailView

from ..substitute import substitute


class CheckSubstituteTestCase(TestCase):
    def setUp(self):
        conserves_category = Category()
        conserves_category.name = 'conserves'
        conserves_category.save()

        abricots_food = Product(id = '49', name = 'abricots', nutrition_grade = 'a')
        abricots_food.save()
        abricots_food.categories.add(conserves_category)
        abricots_food.save()
        self.abricots = abricots_food

        tomates_food = Product(id = '48', name = 'tomates', nutrition_grade = 'b')
        tomates_food.save()
        tomates_food.categories.add(conserves_category)
        tomates_food.save()
        self.tomates = tomates_food

    def test_substitute(self):
        substitute_result = substitute(self.tomates)[0]
        self.assertEqual(substitute_result["name"], self.abricots.name)

    def test_no_substitute(self):
        if substitute(self.abricots):
            substitute_result = substitute(self.abricots)[0]
        else:
            substitute_result = "aucun substitut trouvé"
        self.assertEqual(substitute_result, "aucun substitut trouvé")

