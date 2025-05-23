# Generated by Django 5.1.7 on 2025-03-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="category",
            field=models.CharField(
                choices=[("food", "Food"), ("drink", "Drink"), ("dessert", "Dessert")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/menu_images/"
            ),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
