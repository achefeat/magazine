from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ccal = models.IntegerField()


class Difficulty(models.Model):
    name = models.CharField(max_length=200)


class Type(models.Model):
    name = models.CharField(max_length=200)


class Diet(models.Model):
    name = models.CharField(max_length=200)


class Cuisine(models.Model):
    name = models.CharField(max_length=200)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField('Ingredient')
    method = models.TextField()
    ccal = models.IntegerField()
    time = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)
    rating = models.FloatField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, default=None)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, default=None)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


