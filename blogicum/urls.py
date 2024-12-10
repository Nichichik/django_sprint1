from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Основные страницы блога
    path('pages/', include('pages.urls')),  # Страницы о проекте и правила
]
