# Generated by Django 3.0.2 on 2020-01-14 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_from_original', to='products.Product')),
                ('substitut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_from_substitut', to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
