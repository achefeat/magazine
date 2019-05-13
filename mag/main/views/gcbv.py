from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.http import Http404
from main.serializers import *


class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny, )


class DifficultyList(generics.ListAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes = (AllowAny,)


class DietList(generics.ListCreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    permission_classes = (AllowAny,)


class TypeList(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (AllowAny,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)


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

# class LikeRecipe(generics.CreateAPIView):
#     serializer_class = LikeRecipe
#     permission_classes = (IsAuthenticated,)


class IngredientV(generics.RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)


class CommentV(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

