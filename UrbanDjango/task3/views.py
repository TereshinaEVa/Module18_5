from django.shortcuts import render
from django.views.generic import TemplateView


def platform_menu(request):
    title = 'Главная страница'
    name_str = 'Главная страница'
    context = {
        'title': title,
        'name': name_str
    }
    return render(request, 'third_task/platform.html', context)

def games_menu(request):
    title = 'Магазин'
    context = {
        'title': title,
        'game_1': 'Atomic Heart',
        'game_2': 'Cyberpunk 2077',
        'game_3': 'PayDay 2'
    }
    return render(request, 'third_task/games.html', context)

def cart_str(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'third_task/cart.html', context)