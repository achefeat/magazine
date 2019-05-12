from main.models import *
from main.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404


@api_view(['GET', 'POST'])
def showIngredients(request):
    if request.method == 'GET':
        ing = Ingredient.objects.all()
        serializer = IngredientSerializer(ing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', ])
def like_recipe(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('id'))
    is_liked = False
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        is_liked=False
    else:
        recipe.likes.add(request.user)
        is_liked=True
    return Http404


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