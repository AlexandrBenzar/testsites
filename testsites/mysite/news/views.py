from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category

from .forms import NewsForm


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


def view_news(requests, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(requests, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
