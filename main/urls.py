from django.urls import path

from main.apps import MainConfig
from main.views import contact, StudentListView, StudentDetailView

app_name = MainConfig.name

# Пустые кавычки - идем от корня
urlpatterns = [
    path('students/', StudentListView.as_view(), name='index'),
    # path('students/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student')
    # path('view/<int:pk>/', view_student, name='view_student'),
]
