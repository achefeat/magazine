from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


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



class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'name')
        # fields = ('__all__')


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ccal = serializers.IntegerField(read_only=True, required=False)
    # likes = serializers.IntegerField(read_only=True, required=False)
    ingredients = IngredientSerializer(many=True)
    cuisine = CuisineSerializer()
    diet = DietSerializer()
    type = TypeSerializer()
    difficulty = DifficultySerializer()
    photo = serializers.ImageField()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'method', 'ccal', 'time', 'type', 'cuisine', 'likes', 'difficulty', 'diet', 'photo', 'comments', 'created_by')


class LikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    liked_by = UserSerializer(read_only=True)
    recipe = RecipeSerializer(many=True)

    class Meta:
        model = Likes
        fields = ('liked_by', 'recipe')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    recipe = RecipeSerializer(many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('description', 'created_by')