from django.urls import path, include
from chats.views import chats, chat_page, create_chat

urlpatterns = [
    path('', chats, name='chats'),
    path('<int:pk>/', chat_page, name='chat_page'),
    path('create/', create_chat, name='create_chat')
]
