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

def register(request):
    context = []
    if request.method=='GET':
        return render(request, 'register.html', context)
    else:
        def create_character(user):
            context = []
            character = Character(user=user)
            character.user.first_name = user.first_name
            character.user.last_name = user.last_name
            character.user.email = user.email
            character.user.save()
            character.save()
            return character

        user = request.POST['user']
        context['character'] = create_character(user)

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

