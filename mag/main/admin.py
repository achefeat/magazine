from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Type)
admin.site.register(Difficulty)
admin.site.register(Cuisine)
admin.site.register(Comments)
admin.site.register(Diet)
