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


# class LikeSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     liked_by = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Likes
#         fields = ('liked_by')


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    ccal = serializers.IntegerField(read_only=True, required=False)
    # likes = UserSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(many=True)
    cuisine = CuisineSerializer()
    diet = DietSerializer()
    type = TypeSerializer()
    difficulty = DifficultySerializer()
    photo = serializers.ImageField()
    # comments = UserSerializer(read_only=True, many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'method', 'ccal', 'time', 'type', 'cuisine', 'likes', 'difficulty', 'diet', 'photo', 'comments', 'created_by')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    recipe = RecipeSerializer(many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('id','description', 'created_by')
