from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ccal = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(read_only=True)
    # created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = ('__all__')


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('__all__')

class DifficultySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Difficulty
        fields = ('__all__')


class DietSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Diet
        fields = ('__all__')


class CuisineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cuisine
        fields = ('__all__')


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Type
        fields = ('__all__')