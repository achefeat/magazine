from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ccal = models.IntegerField()

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name ='Difficulty'
        verbose_name_plural ='Difficulties'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Diet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    method = models.TextField()
    ccal = models.IntegerField()
    time = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)
    rating = models.IntegerField(default=None, null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, default=None)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, default=1)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

