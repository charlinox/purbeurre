from django.db import models

class ProductManager(models.Manager):
    """ Create managers for products """

    def create_from_openfoodfacts(
        self,
        code,
        product_name,
        nutrition_grade_fr,
        url,
        image_url,
        image_nutrition_url,
        categories,
        **kwargs):
        """Create products from openfoodfacts data."""
        
        from products.models import Category
         
        if not (
            product_name.strip()
            and nutrition_grade_fr.strip()
            and url.strip()
            and image_url.strip()
            and image_nutrition_url.strip()
            # and ou or ?? on avait mis "or" pour le P5
            ):
            raise TypeError("product_name, nutrition_grade_fr, url, image_url"
                            "and image_nutrition_url must be non-blank fields")
        if len(str(code)) > 19:
            raise TypeError("product.id is too big")

        product = self.get_or_create(
            id=code.strip(),
            name=product_name.lower().strip(),
            nutrition_grade=nutrition_grade_fr.lower().strip(),
            url=url.lower().strip(),
            image_url=image_url.lower().strip(),
            image_nutrition_url=image_nutrition_url.lower().strip()
        )

        for category in categories.split(','):
            category = Category.objects.get_or_create(
                name=category.lower().strip()
            )
            product.categories.add(category)

        return product
