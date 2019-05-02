from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('homerecipes/', views.RecipeV.as_view()),
    path('homerecipes/newrecipe/', views.RecipeNewV.as_view()),
    path('homerecipes/ingredients/', views.IngredientV.as_view()),
    path('homerecipes/difficulty/', views.DifficultyV.as_view()),
    path('homerecipes/cuisine/',views.CuisineV.as_view()),
    path('homerecipes/type/', views.TypeV.as_view()),
    path('homerecipes/diet/',views.DietV.as_view())
]