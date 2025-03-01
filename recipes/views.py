from django.shortcuts import render, get_object_or_404, redirect
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm


def home(request):
    # Получаем все рецепты
    all_recipes = Recipe.objects.all()
    # Выбираем случайные 5 (или меньше, если в базе мало)
    random_recipes = random.sample(list(all_recipes), min(len(all_recipes), 5))
    context = {
        'recipes': random_recipes
    }
    return render(request, 'recipes/index.html', context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/detail.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # сохраняем пользователя
            login(request, user)  # сразу логиним
            return redirect('home')  # перенаправляем на главную
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})

@login_required
def logout_view(request):
    """
    Разлогинивает пользователя и перенаправляет на главную.
    """
    logout(request)        # уничтожаем сессию
    return redirect('home')  # после логаута переходим на главную страницу

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', recipe_id=new_recipe.id)
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Добавить рецепт'})
