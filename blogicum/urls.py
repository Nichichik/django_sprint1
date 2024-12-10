from django.contrib import admin
from django.urls import path, include
from blog.models import Post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Основные страницы блога
    path('pages/', include('pages.urls')),  # Страницы о проекте и правила
]
