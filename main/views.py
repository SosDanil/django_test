from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


class StudentListView(ListView):
    model = Student


# Функцию индекса заменили классовым методом - FBV сменили на CBV

# def index(request):
#     students_list = Student.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная'
#     }
#     return render(request, 'main/student_list.html', context)


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


# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item,
#     }
#     return render(request, 'main/student_detail.html', context)

class StudentCreateView(CreateView):
    model = Student
    # fields = ('first_name', 'last_name', 'avatar') заменяем на работу с формами
    form_class = StudentForm
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    # fields = ('first_name', 'last_name', 'avatar')
    form_class = StudentForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        subject_formset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            # передаем instance только в редактировании
            context_data['formset'] = subject_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = subject_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:index'))
