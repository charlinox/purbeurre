#!/usr/bin/python3
# coding: utf-8

import requests

from django.core.management.base import BaseCommand, CommandError


CATEGORY_LIST = ["pizzas", "choucroutes", "cassoulets"]

class ProductDownloader:

    def fetch(self, categories, number=20):
        payload = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": categories,
            "page_size": number,
            "json": 1,
        }

        response = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl", params=payload)
        data = response.json()
        return data['products']

def create_from_openfoodfacts(cls, code, product_name, nutrition_grades,
                                url, categories, **kwargs):
    """Creates products from openfoodfacts data."""
    if not (product_name.strip() or nutrition_grades.strip():
        raise TypeError("product_name, nutrition_grades and stores must"
                        " be non-blank fields")
    if len("%s" % code) > 19:
        raise TypeError("product.id is too big")

    product = cls.objects.get_or_create(
        name=product_name.lower().strip(),
        nutrition_grade=nutrition_grades.lower().strip(),
        url=url.lower().strip(),
        id=code
    )
    for store in stores.split(','):
        store = Store.objects.get_or_create(
            name=store.lower().strip()
        )
        cls.objects.add_store(product, store)

    for category in categories.split(','):
        category = Category.objects.get_or_create(
            name=category.lower().strip()
        )
        cls.objects.add_category(product, category)
    return product


class Command(BaseCommand):

    def handle(self):
        downloader = ProductDownloader()
        for each_category in CATEGORY_LIST:
            products = downloader.fetch(each_category, 500)
            for product in products:
                try:
                    product = Products.create_from_openfoodfacts(**product)
                except TypeError:
                    continue

