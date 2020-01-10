from django.db import models

class Favorite(models.Model):
    substitut_id = models.ForeignKey("products.Products", on_delete=models.CASCADE)
    original_id = models.ForeignKey("products.Products", on_delete=models.CASCADE)
    # PRIMARY KEY (substitut_id, original_id)

    def __str__(self):
        return self.titre

    class Meta:
        abstract=True