from django.test import TestCase, Client
from ..models import Category, Product
from ..views import result, DetailView

from ..substitute import substitute


class CheckSubstituteTestCase(TestCase):
    def setUp(self):
        conserves_category = Category()
        conserves_category.name = 'conserves'
        conserves_category.save()
        abricots_food = Product(id = '3245412718649', name = 'abricots', nutrition_grade = 'a')
        abricots_food.save()
        abricots_food.categories.add(conserves_category)
        abricots_food.save()
        self.abricots = abricots_food
        tomates_food = Product(id = '3245412718648', name = 'tomates', nutrition_grade = 'b')
        tomates_food.save()
        tomates_food.categories.add(conserves_category)
        tomates_food.save()
        self.tomates = tomates_food

    def test_substitute(self):
        substitute_result = substitute(self.tomates)[0]
        # print (substitute_result, self.abricots.name)
        self.assertEqual(substitute_result.name, self.abricots.name)

    def test_no_substitute(self):
        substitute_result = substitute(self.abricots)[0]
        # print (substitute_result, self.abricots.name)
        self.assertEqual(substitute_result.name, self.tomates.name)

