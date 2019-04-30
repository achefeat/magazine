from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.http import Http404
from main.models import Recipe, Ingredient, Difficulty, Diet, Type, Cuisine
from main.serializers import *
# Create your views here.


class RecipeV(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        return RecipeSerializer

    # def perform_create(self, serializer):


# class IngredientV(generics.)