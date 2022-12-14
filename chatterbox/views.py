from django.http import HttpResponse
from django.shortcuts import render

from chatterbox.models import Room, Message


# Create your views here.
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')

def home(request):
    rooms = Room.objects.all() # najde vsechny mistnosti

    context = {'rooms': rooms}
    return render(request, 'chatterbox/home.html', context)


def search(request, s):
    rooms = Room.objects.filter(name__contains=s)
    messages = Message.objects.filter(body__contains=s)

    context = {'rooms': rooms, 'messages': messages}
    return render(request, "chatterbox/search.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk) # najdeme mistnost se zadanym id
    messages = Message.objects.filter(room=pk)
    context = {'room': room, 'messages': messages}
    return render(request, "chatterbox/room.html", context)