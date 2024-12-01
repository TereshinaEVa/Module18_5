from django.shortcuts import render
from .forms import UserRegister

users = ['Eva', 'Nik']

def sing_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if login in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(login)
                info['message'] = f'Приветствуем, {login}!'
    else:
        form = UserRegister()
        info['message'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sing_up_by_html(request):
    info = {}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if login in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            users.append(login)
            info['message'] = f'Приветствуем, {login}!'
    return render(request, 'fifth_task/registration_page.html', info)
