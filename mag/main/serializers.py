from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'ccal')
        # fields = ('__all__')


class DifficultySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Difficulty
        fields = ('id', 'name')


class DietSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Diet
        fields = ('id', 'name')
        # fields = ('__all__')


class CuisineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cuisine
        fields = ('name', 'id')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cuisine
        fields = ('description', 'id')


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'name')
        # fields = ('__all__')

# class PhotoSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
class LikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    time = serializers.IntegerField(required=False)
    method = serializers.CharField(required=False)
    ccal = serializers.IntegerField(read_only=True, required=False)
    likes = serializers.IntegerField(read_only=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)
    cuisine = CuisineSerializer(required=False)
    diet = DietSerializer(required=False)
    type = TypeSerializer(required=False)
    difficulty = DifficultySerializer(required=False)
    photo = serializers.ImageField(required=False)
    comments = CommentSerializer()

    class Meta:
        model = Recipe
        fields = ('__all__')


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ccal = serializers.IntegerField(read_only=True, required=False)
    likes = serializers.IntegerField(read_only=True, required=False)
    ingredients = IngredientSerializer(many=True)
    cuisine = CuisineSerializer()
    diet = DietSerializer()
    type = TypeSerializer()
    difficulty = DifficultySerializer()
    photo = serializers.ImageField()
    comments = CommentSerializer()
    # created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'method', 'ccal', 'time', 'type', 'cuisine', 'likes', 'difficulty', 'diet', 'photo')