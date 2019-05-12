from .ser import *


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


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Type
        fields = ('id', 'name')
        # fields = ('__all__')


class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.HiddenField(
        write_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = ('liked_by', 'recipe',)


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
        fields = (
            'id', 'name', 'ingredients', 'method', 'ccal', 'time', 'type', 'cuisine', 'likes', 'difficulty', 'diet',
            'photo', 'comments', 'created_by')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    recipe = RecipeSerializer(many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'description', 'created_by')
