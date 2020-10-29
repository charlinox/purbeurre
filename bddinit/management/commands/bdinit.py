#!/usr/bin/python3
# coding: utf-8

import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from products.models import Product

CATEGORY_LIST = [
    "Conserves",
    "Plats préparés",
    "Fruits",
    "desserts",
    "poissons",
    "Légumes et dérivés",
    "Céréales et dérivés",
    "Produits laitiers",
    "viandes",
    "boissons"
]


class ProductDownloader:
    """ Download products from OFF API """

    def fetch(self, categorie, number=20):
        """ Fetch products from OFF API """
        payload = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": categorie,
            "page_size": number,
            "json": 1,
        }

        response = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl", params=payload)
        data = response.json()
        return data['products']


class Command(BaseCommand):

    def handle(self, *args, **options):
        downloader = ProductDownloader()
        for each_category in CATEGORY_LIST:
            products = downloader.fetch(each_category, 500)
            for product in products:
                try:
                    product = Product.objects.create_from_openfoodfacts(
                        **product)
                except TypeError:
                    continue
