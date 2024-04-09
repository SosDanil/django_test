from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    # Должен возвращать http response с помощью функции render
    return render(request, 'main/index.html')
