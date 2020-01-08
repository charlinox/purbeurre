#!/usr/bin/python3
# coding: utf-8

import requests


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

from files.models import Product
# from files.openfoodfacts import ProductDownloader
# from files.constants import *
       
def bddinit():
    downloader = ProductDownloader()
    for each_category in CATEGORY_LIST:
        products = downloader.fetch(each_category, 1000)
        for product in products:
            try:
                product = Product.create_from_openfoodfacts(**product)
            except TypeError:
                continue

