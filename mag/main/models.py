from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    ccal = models.IntegerField()

    def __str__(self):
        return self.name
#
#
# class Likes(models.Model):
#     liked_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#
#     def __str__(self):
#         name = 'likes'
#         return name
#
#     class Meta:
#         verbose_name= 'Like'
#         verbose_name_plural= 'Likes'


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
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    difficulty = models.ForeignKey(Difficulty, on_delete=models.DO_NOTHING, default=None)
    diet = models.ForeignKey(Diet, on_delete=models.DO_NOTHING, default=1)
    photo = models.ImageField(upload_to='media', default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Comments(models.Model):
    description = models.TextField(max_length=700)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None, related_name='comments')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name ='Comment'
        verbose_name_plural ='Comments'

