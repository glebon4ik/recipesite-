from .views import recipe_create
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    
    # Создание нового рецепта
    path('recipe/add/', recipe_create, name='recipe_create'),

    # Регистрация (если у тебя есть)
    path('register/', views.register, name='register'),

    # ЛОГАУТ (наша собственная вьюшка)
    path('logout/', views.logout_view, name='logout'),
]
