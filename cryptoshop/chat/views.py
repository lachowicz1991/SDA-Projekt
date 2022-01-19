from django.shortcuts import render
from .models import Message
from cart.utils import cartData


def index(request):
    data = cartData(request)
    cartitems = data['cartitems']
    return render(request, 'chat/index.html', {'cartitems':cartitems})


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]
    data = cartData(request)
    cartitems = data['cartitems']
    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages, 'cartitems':cartitems})

# @login_required(redirect_field_name= 'accounts/login/')