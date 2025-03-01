from django.db import models
from django.contrib.auth.models import User  # импортируем встроенную модель пользователя

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Можно добавить и другие поля на свое усмотрение, например slug, описание и т.д.

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    instructions = models.TextField(verbose_name="Шаги приготовления", blank=True, null=True)
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (мин)", blank=True, null=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    
    # Связь «многие ко многим» (рецепт может относиться к нескольким категориям)
    categories = models.ManyToManyField(Category, related_name='recipes', blank=True)
    
    # Можно сделать поле для ингредиентов
    ingredients = models.TextField(verbose_name="Ингредиенты", blank=True, null=True)

    def __str__(self):
        return self.title
