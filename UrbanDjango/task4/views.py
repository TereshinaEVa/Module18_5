from django.shortcuts import render
from django.views.generic import TemplateView


def platform_menu(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)

def games_menu(request):
    title = 'Магазин'
    context = {
        'title': title,
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/games.html', context)

def cart_str(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/cart.html', context)