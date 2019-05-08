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
        fields = ('id', 'name')
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
    rating = serializers.IntegerField(read_only=True, required=False)
    ingredients = IngredientSerializer(many=True)
    cuisine = CuisineSerializer()
    diet = DietSerializer()
    type = TypeSerializer()
    difficulty = DifficultySerializer()
    # created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'method', 'ccal', 'time', 'type', 'cuisine', 'rating', 'difficulty', 'diet')