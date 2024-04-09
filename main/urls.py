from django.urls import path

from main.views import index

# Пустые кавычки - идем от корня
urlpatterns = [
    path('', index)
]
