from django.shortcuts import render


def homepage_view(request):
    print(type(render))
    return render(request, 'main/homepage.html', {
        "name": "DJANGO"
    })


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
