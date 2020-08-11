from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.
# Views-контроллер вызывается в ответ на клиентский запрос. Обрабатывет запрос, формирует данные запрашивая их у модели
# и возвращает ответ в виде представления заполненного данными. КОнтроллер связуещее звено
# между данными и их отображениями

def index(requests):
    # print(requests)
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей', }
    return render(requests, 'news/index.html', context=context)


def get_category(requests, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news,
               'category': category, }
    return render(requests, 'news/category.html', context=context)
