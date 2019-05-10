from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from main.models import Recipe, Ingredient, Difficulty, Diet, Type, Cuisine
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)


# class RecipeDetail(generics.ListAPIView):
#     serializer_class = RecipeSerializer


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)


class DifficultyList(generics.ListCreateAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes = (IsAuthenticated,)


class DietList(generics.ListCreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    permission_classes = (IsAuthenticated,)


class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['POST', ])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST', ])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)


class CuisineList(generics.ListCreateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = (IsAuthenticated,)


class CommentDetail(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            recipe = Recipe.objects.get(id=self.kwargs['pk'])
        except Comments.DoesNotExist:
            raise Http404
        return recipe.comments.all()


# =========================================
# class UserV(generics.RetrieveDestroyAPIV)


class RecipeV(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)


class IngredientV(generics.RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)


class CommentV(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class LikeView(APIView):
    permission_classes = (IsAuthenticated,)

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
