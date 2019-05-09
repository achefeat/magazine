from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/recipelist/', views.RecipeList.as_view()),
    path('home/recipe/', views.RecipeV.as_view()),

    path('home/ingredientlist/', views.IngredientList.as_view()),
    path('home/ingredient/', views.IngredientV.as_view()),

    path('home/difficultylist/', views.DifficultyList.as_view()),
    # path('home/difficulty/', views.DifficultyV.as_view()),

    path('home/cuisinelist/',views.CuisineList.as_view()),
    path('home/cuisine/', views.CuisineV.as_view()),

    path('home/typelist/', views.TypeList.as_view()),
    # path('home/type/', views.TypeV.as_view()),

    path('home/dietlist/',views.DietList.as_view()),
    path('home/diet/',views.DietV.as_view()),

    path('home/recipe/like/<int:pk>/', views.LikeView.as_view()),
    path('home/recipe/comments/<int:pk>/', views.CommentList.as_view()),

]