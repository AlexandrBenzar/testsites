from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail

from .models import News, Category

from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm

from .utils import MyMixin


# Create your views here.
# Views-контроллер вызывается в ответ на клиентский запрос. Обрабатывет запрос, формирует данные запрашивая их у модели
# и возвращает ответ в виде представления заполненного данными. КОнтроллер связуещее звено
# между данными и их отображениями

def register(requests):
    if requests.method == 'POST':
        form = UserRegisterForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            messages.success(requests, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(requests, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(requests, 'news/register.html', {'form': form})


def user_login(requests):
    if requests.method == 'POST':
        form = UserLoginForm(data=requests.POST)
        if form.is_valid():
            user = form.get_user()
            login(requests, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(requests, 'news/login.html', {'form': form})


def user_logout(requests):
    logout(requests)
    return redirect('login')


def contact(requests):
    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'casha199410@gmail.com',
                             ['albenzar@bk.ru'], fail_silently=True)
            if mail:
                messages.success(requests, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(requests, 'Ошибка отправки')
        else:
            messages.error(requests, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(requests, 'news/test_email.html', {'form': form})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 10

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(s='Главная страница')
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    raise_exception = True

# def index(requests):
#     # print(requests)
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей', }
#     return render(requests, 'news/index.html', context=context)


# def get_category(requests, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {'news': news,
#                'category': category, }
#     return render(requests, 'news/category.html', context=context)


# def view_news(requests, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(requests, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
