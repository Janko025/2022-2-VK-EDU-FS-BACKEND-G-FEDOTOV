from django.urls import path, include

from main.views import main_page

urlpatterns = {
    path('', main_page, name='main_page'),
    path('chats/', include('chats.urls')),
}