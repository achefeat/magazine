from main.models import *
from main.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class RecipeList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        recipeList = Recipe.objects.all()
        serializer = RecipeSerializer(recipeList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RecipeV(APIView): #heeeeelp

    def get_object(self, pk):
        try:
            return Recipe.objects.get(id=pk)
        except Recipe.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(instance=recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

