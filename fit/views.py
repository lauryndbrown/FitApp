from django.shortcuts import render

def index(request):
    context = []
    return render(request, 'index.html', context)

def about(request):
    context = []
    return render(request, 'about.html', context)

def game(request):
    context = []
    return render(request, 'game.html', context)

def character(request):
    context = []
    return render(request, 'game.html', context)

def shop(request):
    context = []
    return render(request, 'shop.html', context)

def adventure(request):
    context = []
    return render(request, 'adventure.html', context)

