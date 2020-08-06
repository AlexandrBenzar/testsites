from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.
# Views-контроллер вызывается в ответ на клиентский запрос. Обрабатывет запрос, формирует данные запрашивая их у модели
# и возвращает ответ в виде представления заполненного данными. КОнтроллер связуещее звено
# между данными и их отображениями

def index(requests):
    # print(requests)
    news = News.objects.all()
    return render(requests, 'news/index.html', {'news': news, 'title': 'Список новостей'})

