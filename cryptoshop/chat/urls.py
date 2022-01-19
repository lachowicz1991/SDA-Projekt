
from django.urls import path

from .views import index, room

urlpatterns = [
    path('chat', index, name='chat'),
    path('chat/<str:room_name>/', room, name='room'),
]