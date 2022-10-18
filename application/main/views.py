from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    if request.method == 'GET':
        return render(request, template_name='main/main_page.html')
    else:
        return HttpResponse(status=405)