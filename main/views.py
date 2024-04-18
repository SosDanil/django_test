from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'


# Функцию индекса заменили классовым методом - FBV сменили на CBV

# def index(request):
#     students_list = Student.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная'
#     }
#     return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    # Должен возвращать http response с помощью функции render
    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item,
#     }
#     return render(request, 'main/student_detail.html', context)

class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')

