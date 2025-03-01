from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # подключаем наши "recipes/urls.py"
    
    # Логин (если ты оставляешь авторизацию через LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
