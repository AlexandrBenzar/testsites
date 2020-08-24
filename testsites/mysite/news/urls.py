from django.urls import path
from .views import contact, register, user_login, user_logout, HomeNewsView, NewsByCategoryView, NewsView, \
    CreateNewsView

urlpatterns = [
    # path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeNewsView.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategoryView.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', NewsView.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNewsView.as_view(), name='add_news'),
]
