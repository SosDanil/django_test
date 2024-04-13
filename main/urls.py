from django.urls import path

from main.apps import MainConfig
from main.views import index, contact

app_name = MainConfig.name

# Пустые кавычки - идем от корня
urlpatterns = [
    path('students/', index, name='index'),
    path('contact/', contact, name='contact'),
]
