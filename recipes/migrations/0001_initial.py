# Generated by Django 5.1.6 on 2025-03-01 19:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('instructions', models.TextField(blank=True, null=True, verbose_name='Шаги приготовления')),
                ('cooking_time', models.PositiveIntegerField(blank=True, null=True, verbose_name='Время приготовления (мин)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe_images/')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='Ингредиенты')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('categories', models.ManyToManyField(blank=True, related_name='recipes', to='recipes.category')),
            ],
        ),
    ]
