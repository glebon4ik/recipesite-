from django.contrib import admin
from .models import Recipe, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cooking_time']
    # Если хочешь, можешь также добавить поля поиска, фильтры, т.д.
    search_fields = ['title', 'description']
    list_filter = ['categories']
