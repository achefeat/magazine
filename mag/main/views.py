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


# class RecipeDetail(generics.ListAPIView):
#     serializer_class = RecipeSerializer


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


class CommentDetail(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            recipe = Recipe.objects.get(id=self.kwargs['pk'])
        except Comments.DoesNotExist:
            raise Http404
        return recipe.comments.all()


# =========================================


class RecipeV(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientV(generics.RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


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
