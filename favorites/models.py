from django.db import models
from django.contrib.auth.models import User


class Favorite(models.Model):
    substitut = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_from_substitut")
    original = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_from_original")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorites")

    # PRIMARY KEY (substitut_id, original_id)

    def __str__(self):
        return self.user
