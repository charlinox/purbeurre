#!/usr/bin/python3
# coding: utf-8

import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import models

CATEGORY_LIST = [
    "Conserves",
    "Plats préparés",
    "Fruits",
    "Légumes et dérivés",
    "Céréales et dérivés",
    "Produits laitiers"
    ]

class ProductDownloader:
    """ Download products from OFF API """

    def fetch(self, categories, number=20):
        """ Fetch products from OFF API """
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

class ProductManager(models.Manager):
    """ Create managers for products """

    def create_from_openfoodfacts(
        # code, plus besoin du code j'imagine
        product_name,
        nutrition_grades,
        url,
        image_url,
        image_nutrition_url,
        categories,
        **kwargs):
        """Create products from openfoodfacts data."""
        
        if not (
            product_name.strip()
            and nutrition_grades.strip()
            and url.strip()
            and image_url.strip()
            and image_nutrition_url.strip()
            # and ou or ?? on avait mis "or" pour le P5
            ):
            raise TypeError("product_name, nutrition_grades, url, image_url"
                            "and image_nutrition_url must be non-blank fields")
        # if len("%s" % code) > 19:
        #     raise TypeError("product.id is too big")

        product = Products.objects.get_or_create(
            name=product_name.lower().strip(),
            nutrition_grade=nutrition_grades.lower().strip(),
            url=url.lower().strip(),
            image_url=image_url.lower().strip(),
            image_nutrition_url=image_nutrition_url.lower().strip(),
            # id=code
        )

        for category in categories.split(','):
            category = Category.objects.get_or_create(
                # Est il vraiment necessaire d'instancier dans ce cas là ?
                name=category.lower().strip()
            )
            product_categories.objects.get_or_create(
                product_id=product.id,
                category_id=category.id
            )

        return product


class Command(BaseCommand):

    def handle(self):
        downloader = ProductDownloader()
        for each_category in CATEGORY_LIST:
            products = downloader.fetch(each_category, 500)
            for product in products:
                try:
                    product = Products.objects.create_from_openfoodfacts(**product)
                except TypeError:
                    continue

