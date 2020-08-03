from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Views-контроллер вызывается в ответ на клиентский запрос. Обрабатывет запрос, формирует данные запрашивая их у модели
# и возвращает ответ в виде представления заполненного данными. КОнтроллер связуещее звено
# между данными и их отображениями

def index(requests):
    # print(requests)
    return HttpResponse('Hello World')

def test(requests):
    # print(requests)
    return HttpResponse('<h1>Тестовая страница</h1>')
