from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from main.models import Recipe, Ingredient, Difficulty, Diet, Type, Cuisine
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # @property
    # def calories(self):
    #     return self.ingredients.id


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class DifficultyList(generics.ListCreateAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class DietList(generics.ListCreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer


class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CuisineList(generics.ListCreateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

# =========================================


class RecipeV(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientV(generics.RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# class DifficultyV(generics.RetrieveUpdateAPIView):
#     queryset = Difficulty.objects.all()
#     serializer_class = DifficultySerializer


class DietV(generics.RetrieveUpdateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer


# class TypeV(generics.RetrieveUpdateAPIView):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer


class CuisineV(generics.RetrieveUpdateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


class CommentV(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class LikeView(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(id=pk)
        except Recipe.DoesNotExist as e:
            raise Http404

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = LikeSerializer(instance=recipe, data=request.data)
        if serializer.is_valid():
            recipe.likes +=1
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
