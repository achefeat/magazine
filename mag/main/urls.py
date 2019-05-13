from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # cbv
    path('home/recipelist/', views.RecipeList.as_view()),
    path('home/recipe/<int:pk>/', views.RecipeV.as_view()),
    # gcbv
    path('home/ingredient/', views.IngredientV.as_view()),
    path('home/difficultylist/', views.DifficultyList.as_view()),
    path('home/userlist/', views.UserList.as_view()),
    path('home/cuisinelist/', views.CuisineList.as_view()),
    path('home/typelist/', views.TypeList.as_view()),
    path('home/dietlist/', views.DietList.as_view()),
    path('home/recipe/<int:pk>/comments/', views.CommentDetail.as_view()),
    path('home/likes/', views.LikeCreate.as_view()),
    # fbv
    path('home/signup/', views.signup),
    path('home/ingredientlist/', views.showIngredients),
    path('home/login/', views.login),
    path('home/logout/', views.logout),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
