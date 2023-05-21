from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    template = "predict/index.html"
    title = "Главная страница"
    description = "Главная страница сайта!"
    context = {
        "description": description,
        "title": title,
    }
    return render(request, template, context)


def seasons(request):
    template = "predict/seasons.html"
    title = "Сезоны"
    graphics = "Тут будут графики сезоны. МНОГО!"
    context = {
        "graphics": graphics,
        "title": title,
    }
    return render(request, template, context)


def dynamics(request):
    template = "predict/dynamic.html"
    title = "Динамика спроса"
    graphics = "Тут будут графики динамика спроса. МНОГО!"
    context = {
        "graphics": graphics,
        "title": title,
    }
    return render(request, template, context)


def profile_demand(request):
    template = "predict/demand.html"
    title = "Динамика спроса"
    graphics = "Тут будут графики профиль спроса. МНОГО!"
    context = {
        "graphics": graphics,
        "title": title,
    }
    return render(request, template, context)
