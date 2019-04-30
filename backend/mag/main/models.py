from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ccal = models.IntegerField()
    recipes = models.ManyToManyField('Recipe', related_name='ingr_of_rec')


class Difficulty(models.Model):
    name = models.CharField(max_length=200)
    # recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipes = models.ManyToManyField('Recipe', related_name='diff_of_rec')


class Type(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField('Recipe', related_name='type_of_rec')


class Diet(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField('Recipe', related_name='diet_of_rec')


class Cuisine(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField('Recipe', related_name='cuis_of_rec')


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField('Ingredient', related_name='rec_of_ingr')
    method = models.TextField()
    ccal = models.IntegerField()
    time = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)
    rating = models.FloatField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, default=None)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


