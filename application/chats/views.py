from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def chats(request):
    if request.method == 'GET':
        return JsonResponse({'chats:': []})
    else:
        return HttpResponse(status=405)

def chat_page(request, pk):
    if request.method == 'GET':
        return JsonResponse({'chat': pk})
    else:
        return HttpResponse(status=405)
def create_chat(request):
    if request.method == 'GET':
        return JsonResponse({'log': 'janko@25.ru', 'password': '1234'})
    else:
        return HttpResponse(status=405)